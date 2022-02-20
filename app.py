from flask import Flask, render_template, Response, request
import mediapipe as mp
import numpy as np
import cv2
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english.conversations")
trainer.train("chatterbot.corpus.custom.myown")

doneCheck = 1


def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Squat Counter variables
squatTrue = True
squatLeftCounter = 0
squatLeftStage = None
squatRightCounter = 0
squatRightStage = None


def gen_frames2():  # generate frame by frame from camera
    global squatTrue, squatLeftCounter, squatLeftStage, squatRightCounter, squatRightStage
    cap = cv2.VideoCapture(0)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=1) as pose:
        while cap.isOpened():
            try:
                ret, frame = cap.read()
            except Exception as e:
                print(str(e))
                continue
            image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if squatTrue:
                try:
                    landmarks = results.pose_landmarks.landmark

                    # Get coordinates
                    leftHip = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    leftKnee = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                    leftAnkle = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                                 landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                    rightHip = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    rightKnee = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                    rightAnkle = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                                  landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                    # Calculate angle
                    rightAngle = calculate_angle(rightHip, rightKnee, rightAnkle)
                    leftAngle = calculate_angle(leftHip, leftKnee, leftAnkle)

                    # Visualize angle
                    cv2.putText(image, str(rightAngle),
                                tuple(np.multiply(rightKnee, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )
                    cv2.putText(image, str(leftAngle),
                                tuple(np.multiply(leftKnee, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )

                    if leftAngle < 90:
                        squatLeftStage = "down"
                    if leftAngle > 100 and squatLeftStage == 'down':
                        squatLeftStage = "up"
                        squatLeftCounter += 1
                        print("Left:" + str(squatLeftCounter))

                    if rightAngle < 90:
                        squatRightStage = "down"
                    if rightAngle > 100 and squatRightStage == 'down':
                        squatRightStage = "up"
                        squatRightCounter += 1
                        print("Right:" + str(squatRightCounter))

                except Exception as e:
                    print(str(e))

                # cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)
                cv2.putText(image, 'Left REPS', (15, 12),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(squatLeftCounter), (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(image, 'STAGE', (125, 12),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, squatLeftStage, (120, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

                cv2.putText(image, 'Right REPS', (15, 82),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(squatRightCounter), (10, 130),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(image, 'STAGE', (125, 82),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, squatRightStage, (120, 130),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )

            ret, buffer = cv2.imencode('.jpg', image)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed2')
def video_feed2():
    # Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames2(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/back')
def back():
    return render_template('background.html')


@app.route('/loginPage')
def login():
    return render_template('loginPage.html')


@app.route('/dizzy')
def dizzi():
    return render_template('dizzy.html', value=doneCheck)


@app.route('/dizzy-result')
def dizziResult():
    return render_template('dizzy-result.html', value=round(squatRightCounter + squatLeftCounter, 2))


@app.route('/driving')
def driving():
    return render_template('driving.html')


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(threaded=True, port=5500)

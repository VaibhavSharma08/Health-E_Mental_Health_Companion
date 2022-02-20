## How to Run
After downloading all files, run the command "pip install -r requirements.txt". Go to the folder named "Server for transcription" and enter command "npm run server". Now run "python app.py" in another terminal.


## Inspiration
Feeling mentally down and depressed? Feeling fatigued and unfit and haven't exercised in ages? Worry not for Health-E will help you overcome all these hurdles and make you fit again. 
Looking at the meteoric rise inn mental health issues in today's world, we have created a Personal Mental HealthCare Companion for people which will help them recover faster, heal better and become stronger. 

Our application helps keep a person motivated, gives them access to real time facts and figures, monitors their recovery exercises and helps regulate their diet along with a number of other features and is of vital importance.

## What it does
We have created a web application which aims to streamline the recovery process of an ill person and help them recover faster while not giving in to depression or anxiety. The app has a number of features as explained below:

-> A proper healthy diet is essential for fast recovery and regaining bodily strength. Our app will **help regulate the user’s diet by providing a diet plan according to the symptoms and current condition of the user.**

-> The app will include **an interactive chatbot which provides answers to a plethora of queries including but not limited to getting current facts and figures about the disease, FAQs, useful tips, etc.** 

-> The app will also include **an AI-based exercise section containing a number of exercises which the user can choose from.** Once chosen, **the app then monitors the user while exercising and alerts the user in case of incorrect method and posture. All this is done using advanced AI algorithms for detecting posture and pose.**

## How we built it
-> The web application has been created using AssemblyAI's API, Flask, HTML, CSS, Javascript, OpenCV and Mediapipe.

-> The pose and posture detection and correction is done using OpenCV for capturing the videostream and sending it to the Python backend and Mediapipe for running the advanced AI algorithms using models created in Tensorflow.

-> The chatbot has also been created in Python and uses ChatterBox module with the feature of Speech to Text implemented via AssemblyAI's API.

-> The front facing website which contains these features has been created using HTML, CSS and Javascript and uses Flask as its backend. As the user proceeds through the website, the respective features are shown to the User via Flask.

## Challenges we ran into
It was initially challenging to set up the AI Posture Detection and getting the video stream to work in the Flask Back End. Also, the chatbot integration into the whole project was a challenge since it needed to run on the main thread and couldn't be multithreaded easily.

## What we learned
We learned a lot from this project. We learnt about using flask and in general about the integration of all these components and making them work together. Our research into the current mental health situation of the world also made us more aware.

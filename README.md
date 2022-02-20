## How To Run
For running code, download and execute "requirements.txt" by running the command: pip install -r requirements.txt
Then execute app.py and go to the link which appears in the terminal

## Inspiration
Having to drive while fatigued is one of the prime factors of road accidents worldwide, since even a small mistake can lead to accidents. After witnessing one such accident with our eyes, we thought about it and came up with this product. We hope that as we continue to work on this product and improve it, it can help avert a lot of accidents in the future.

## What it does
Our product uses sophisticated Machine Learning algorithms in order to detect the person's face and eyes. First, the person has to undergo a dizziness test, wherein he/she has to move his face according to the specified point. Through this, we determine whether the person is dizzy or not since we measure the time taken for the specified reflexes. Based on the results, if the person is fit to drive, he/she will then start driving as the product continuously monitors them. What the product does while the person is driving is continuously monitor the person's eyes in order to detect if the person is drowsy or not. When the person is drowsy, the product detects it and issues an alert in the form of an alarm which alerts the user and helps avert any accident the user might have gotten into if the product hadn't been there and he/she continued to be drowsy. Thus, our product helps prevent any untoward incident which might occur due to driving while fatigued.
We are currently using a separate camera for capturing the Video, with the processing being done on a Laptop. Ideally, the user will open our website on his/her phone, undergo the dizziness test and then keep the phone behind the steering wheel so that it captures the person's face continuously.

## How we built it
We used Python as the backend for our product, with Flask handling the video feed and webpages and dlib and OpenCV libraries detecting the Face and Eyes and doing the calculations for Dizziness and Drowsiness detection. The webpages were created with HTML, CSS and Javascript. 

## Challenges we ran into
While creating the product, we faced some problems while integrating the Flask code with our Drowsiness and Dizziness code. What we did to overcome this was go through the code line by line while simultaneously going through the documentation. Ultimately, we did succeed in integrating the detection part with our Flask code.

## Accomplishments that we're proud of
We are really proud of our product since we have put in a lot of effort into developing and integrating it. We also believe that the benefits of our product are endless and once we perfect it, it can usher in a new revolution in terms of safety and accident prevention technology.

## What we learned
We learned a lot from this project. We had to code in Flask from scratch with little to no knowledge. So we learnt how to code in Flask while creating the product. We also upgraded our skills in Machine Learning and OpenCV while working on this product. We also learnt that doing something good for others ultimately translates to doing good for ourselves.

## What's next for Dizztinction: The Real Time Fatigue Detection System
We aim to improve our face and eye detection capabilities with time. We also plan to decrease the latency of the data being transferred to and from the cloud.

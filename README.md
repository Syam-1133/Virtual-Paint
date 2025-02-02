# Virtual-Paint

This project is a virtual paint application that allows users to draw on the screen using hand gestures. It leverages MediaPipe Hands for hand tracking and OpenCV for real-time video processing. The application detects the index finger of the user's hand and uses its position to draw on the screen. Additionally, it includes an erase mode to remove parts of the drawing.

Features
Real-Time Hand Tracking: The application tracks the user's hand in real-time using the MediaPipe Hands solution.

Virtual Drawing: Users can draw on the screen by moving their index finger.

Erase Mode: Toggle erase mode to remove parts of the drawing by moving the index finger over the lines.

Clear Screen: Clear the entire drawing with a single keypress.

User-Friendly Interface: The application displays the current mode (drawing or erasing) on the screen.

How It Works
Hand Detection: The MediaPipe Hands model detects hand landmarks (key points) in the video feed.

Index Finger Tracking: The position of the index finger tip (landmark 8) is used as the drawing tool.

Drawing: As the user moves their index finger, the application records the finger's position and connects the points to create a continuous line.

Erasing: In erase mode, the application removes lines near the index finger's position.

Mode Toggle: The user can toggle between drawing and erasing modes using the 'e' key.

Clear Screen: The 'c' key clears the entire drawing.

Exit: The application can be exited by pressing the 'q' key.

Requirements
Python 3.x

OpenCV (cv2)

MediaPipe (mediapipe)

Installation
Clone the repository:

bash

Install the required libraries:

bash
Copy
pip install opencv-python mediapipe
Run the application:

bash
Copy
python virtual_paint.py
Usage
Launch the application.

Position your hand in front of the camera.

Use your index finger to draw on the screen.

Toggle erase mode by pressing the 'e' key.

Clear the drawing by pressing the 'c' key.

Exit the application by pressing the 'q' key.

Code Explanation
MediaPipe Hands Initialization: The mp.solutions.hands module is used to detect and track hand landmarks.

OpenCV Video Capture: The webcam feed is captured using OpenCV.

Drawing Logic: The application stores the positions of the index finger tip in a list (drawing_points) and connects them to draw lines.

Erase Logic: In erase mode, the application removes lines near the index finger's position by filtering out points close to the finger.

Mode Toggle: The erase_mode flag is toggled using the 'e' key.

Clear Screen: The drawing_points list is cleared when the 'c' key is pressed.

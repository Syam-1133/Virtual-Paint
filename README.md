# Virtual-Paint

Overview:
This project implements a Virtual Paint Application where the user can draw on the screen using hand gestures. The app uses MediaPipe Hands for hand tracking and OpenCV for video capturing and rendering. The user can select different colors or erase the drawing by simply moving their hand over a virtual palette of buttons displayed on the screen.

Key Features:
Hand Gesture Recognition: The app tracks the position of the user's hand using MediaPipe's hand landmarks.
Virtual Drawing: Users can draw on the screen by moving their hand, with the index finger tip acting as the "pen."
Color Selection: The app features a palette of color options (Red, Green, Blue, Yellow) that users can select by hovering their finger over the respective color buttons.
Erase Mode: An "Eraser" button allows users to delete the lines they've drawn by switching to erase mode, which is triggered by hovering the hand over the "Eraser" button.
Dynamic UI: The color palette and erase button are displayed at the top of the screen, and users can interact with them using hand gestures.
Technologies Used:
Python: The core language for this project.
OpenCV: Used for video capture, image processing, and rendering the interactive user interface.
MediaPipe: A framework from Google that provides easy-to-use solutions for hand tracking and other computer vision tasks.
Numpy: A library used for matrix operations and image processing.
How It Works:
Hand Tracking: The project uses MediaPipe Hands, a pre-trained model, to detect and track key landmarks on the user's hand, such as the index finger tip.
Hand Position Mapping: The coordinates of the index finger tip are mapped to the screen, allowing users to draw or interact with buttons on the screen by moving their hand.
Drawing Mechanism: When the index finger tip is within a defined area (near the color buttons), the program registers it as a drawing point. The points are connected by lines, creating the user's drawing.
Color and Eraser Controls: The user can change the color of the drawing by selecting a color from the virtual palette, or they can erase lines by enabling the erase mode via the "Eraser" button.
UI Rendering: The virtual palette is rendered at the top of the screen, and the buttons are interactive based on the user's hand position.
Usage:
Clone the repository to your local machine.
Install the required dependencies using:
bash
Copy
Edit
pip install opencv-python mediapipe numpy
Run the Python script, and the application will open the webcam for real-time hand tracking and drawing.
Use your hand to hover over the color buttons to change the drawing color or activate the erase mode.
Improvements:
Multi-hand support: Currently, the application tracks only one hand. Multi-hand support could be implemented for more complex gestures.
Shape drawing: Future enhancements could include adding shapes (e.g., circles, squares) for more complex drawings.
Save Feature: Implementing an option to save the drawing to an image file.
Demonstration:
In the application, users can see a virtual painting canvas where they can use their hand gestures to draw and select different colors.
The interactive buttons for colors and the eraser are shown at the top of the screen, and hovering the hand over a button will select it.
The color or eraser mode remains active until the user switches it.
Installation & Setup:
Clone the repository:
bash
Copy
Edit
git clone https://github.com/Syam1133/virtual-paint.git
Install dependencies:
bash
Copy
Edit
pip install opencv-python mediapipe numpy
Run the script:
bash
Copy
Edit
python virtualpaint.py

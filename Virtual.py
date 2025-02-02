import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

# Initialize OpenCV video capture
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# List to store drawing points
drawing_points = []
erase_mode = False  # Flag to track erase mode

while True:
    success, img = cap.read()
    if not success:
        print("Error: Could not read frame.")
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Index finger tip (landmark 8)
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            h, w, c = img.shape
            cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

            if erase_mode:
                # Remove lines near the index finger tip
                new_drawing_points = []
                for i in range(1, len(drawing_points)):
                    x1, y1 = drawing_points[i - 1]
                    x2, y2 = drawing_points[i]
                    # Check if the line is near the finger position
                    if abs(cx - x1) > 30 and abs(cy - y1) > 30 and abs(cx - x2) > 30 and abs(cy - y2) > 30:
                        new_drawing_points.append((x1, y1))
                        new_drawing_points.append((x2, y2))
                drawing_points = new_drawing_points
            else:
                # Add index finger tip position to drawing points
                drawing_points.append((cx, cy))

    # Draw all the points on the image
    for i in range(1, len(drawing_points)):
        cv2.line(img, drawing_points[i - 1], drawing_points[i], (0, 260, 0), 4)

    # Display erase mode status
    if erase_mode:
        cv2.putText(img, "Erase Mode: ON", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        cv2.putText(img, "Erase Mode: OFF", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the image
    cv2.imshow("Virtual Paint Syam Drwaing", img)

    # Toggle erase mode with 'e' key
    key = cv2.waitKey(1)
    if key == ord('e'):
        erase_mode = not erase_mode  # Toggle erase mode
        print("Erase Mode:", "On" if erase_mode else "Off")
    elif key == ord('c'):  # Clear the drawing if 'c' is pressed
        drawing_points = []
    elif key == ord('q'):  # Quit if 'q' is pressed
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()


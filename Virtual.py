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
selected_color = (0, 255, 0)  # Default color (green)

# Color options (Red, Green, Blue, Yellow, Eraser)
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 255)]
color_buttons = [(330, 20, "Red"), (430, 20, "Green"), (530, 20, "Blue"), (630, 20, "Yellow"), (730, 20, "Eraser")]


# Function to draw the color palette and erase button
def draw_color_palette(img):
    global selected_color, erase_mode

    for x, y, color_name in color_buttons:
        # Draw color options as rectangles
        color = (0, 0, 0)  # Default black color for text
        color_rect = (x, y, 80, 50)  # Rectangle dimensions for color buttons
        if color_name == "Red":
            color_rect_color = (0, 0, 255)
        elif color_name == "Green":
            color_rect_color = (0, 255, 0)
        elif color_name == "Blue":
            color_rect_color = (255, 0, 0)
        elif color_name == "Yellow":
            color_rect_color = (0, 255, 255)
        elif color_name == "Eraser":
            color_rect_color = (255, 255, 255)  # White color for eraser button

        # Draw the rectangle
        cv2.rectangle(img, (x, y), (x + 80, y + 50), color_rect_color, -1)
        # Draw text on the rectangle
        cv2.putText(img, color_name, (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        # Highlight the selected button
        if color_name == "Red" and selected_color == (0, 0, 255):
            cv2.rectangle(img, (x, y), (x + 80, y + 50), (255, 255, 255), 3)  # White border for selected color
        elif color_name == "Green" and selected_color == (0, 255, 0):
            cv2.rectangle(img, (x, y), (x + 80, y + 50), (255, 255, 255), 3)
        elif color_name == "Blue" and selected_color == (255, 0, 0):
            cv2.rectangle(img, (x, y), (x + 80, y + 50), (255, 255, 255), 3)
        elif color_name == "Yellow" and selected_color == (0, 255, 255):
            cv2.rectangle(img, (x, y), (x + 80, y + 50), (255, 255, 255), 3)
        elif color_name == "Eraser" and erase_mode:
            cv2.rectangle(img, (x, y), (x + 80, y + 50), (255, 255, 255), 3)


# Main loop
while True:
    # Capture video frame
    success, img = cap.read()
    if not success:
        print("Error: Could not read frame.")
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    # Draw the color palette and buttons on the screen
    draw_color_palette(img)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Index finger tip (landmark 8)
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            h, w, c = img.shape
            cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

            # Check if the finger is hovering over any color button
            for x, y, color_name in color_buttons:
                if x <= cx <= x + 80 and y <= cy <= y + 50:
                    if color_name == "Eraser":
                        erase_mode = True
                    else:
                        erase_mode = False
                        if color_name == "Red":
                            selected_color = (0, 0, 255)
                        elif color_name == "Green":
                            selected_color = (0, 255, 0)
                        elif color_name == "Blue":
                            selected_color = (255, 0, 0)
                        elif color_name == "Yellow":
                            selected_color = (0, 255, 255)

            # Draw the current path based on finger position
            if erase_mode:
                # Remove lines near the index finger tip
                new_drawing_points = []
                for i in range(1, len(drawing_points)):
                    x1, y1 = drawing_points[i - 1]
                    x2, y2 = drawing_points[i]
                    if abs(cx - x1) > 30 and abs(cy - y1) > 30 and abs(cx - x2) > 30 and abs(cy - y2) > 30:
                        new_drawing_points.append((x1, y1))
                        new_drawing_points.append((x2, y2))
                drawing_points = new_drawing_points
            else:
                # Add index finger tip position to drawing points
                drawing_points.append((cx, cy))

    # Draw all the points on the image
    for i in range(1, len(drawing_points)):
        cv2.line(img, drawing_points[i - 1], drawing_points[i], selected_color, 4)

    # Display the image
    cv2.imshow("Virtual Paint Syam Drawing", img)

    # Quit if 'q' is pressed
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

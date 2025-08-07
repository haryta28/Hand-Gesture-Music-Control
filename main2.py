import cv2
import mediapipe as mp
import numpy as np
import os
import math
import time

# Initialize MediaPipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)

# Previous volume to smooth changes
prev_volume = -1
prev_time = 0

# Volume control function for macOS using AppleScript
def set_volume(vol_percent):
    vol_percent = max(0, min(100, int(vol_percent)))
    os.system(f"osascript -e 'set volume output volume {vol_percent}'")

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Mirror the image for natural interaction
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            lmList = []
            h, w, _ = img.shape

            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((cx, cy))

            if len(lmList) >= 9:
                x1, y1 = lmList[4]   # Thumb tip
                x2, y2 = lmList[8]   # Index tip

                # Draw circles and line
                cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
                cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 2)

                # Measure distance
                length = math.hypot(x2 - x1, y2 - y1)

                # Convert length to volume
                vol = np.interp(length, [20, 200], [0, 100])
                smooth_vol = round(vol)

                # Only update if change is significant
                if abs(smooth_vol - prev_volume) >= 3:
                    set_volume(smooth_vol)
                    prev_volume = smooth_vol

                # Draw volume bar
                vol_bar = int(np.interp(length, [20, 200], [400, 150]))
                cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 255), 2)
                cv2.rectangle(img, (50, vol_bar), (85, 400), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'{int(vol)}%', (40, 430), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 255, 255), 2)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # FPS counter
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time + 1e-6)
    prev_time = curr_time
    cv2.putText(img, f'FPS: {int(fps)}', (450, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)

    # Show the image
    cv2.imshow("Gesture Volume Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

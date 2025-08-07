import cv2
import mediapipe as mp
import time
import os

# macOS AppleScript for controlling Spotify
def run_applescript(command):
    os.system(f"osascript -e '{command}'")

def play_music():
    run_applescript('tell application "Spotify" to play')

def pause_music():
    run_applescript('tell application "Spotify" to pause')

def next_track():
    run_applescript('tell application "Spotify" to next track')

def previous_track():
    run_applescript('tell application "Spotify" to previous track')

def volume_up():
    os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) + 10)'")

def volume_down():
    os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) - 10)'")

# Mediapipe setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

prev_time = 0
gesture = None

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            # Get landmark positions
            lm_list = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            # Detect simple gestures based on finger positions
            if lm_list:
                # Thumb tip and index tip distance
                thumb = lm_list[4]
                index = lm_list[8]
                middle = lm_list[12]
                pinky = lm_list[20]

                distance = ((thumb[0] - index[0])**2 + (thumb[1] - index[1])**2) ** 0.5

                # Open hand = Play
                if index[1] < middle[1] < pinky[1]:
                    if gesture != "play":
                        play_music()
                        gesture = "play"

                # Fist = Pause
                elif index[1] > thumb[1] and middle[1] > thumb[1]:
                    if gesture != "pause":
                        pause_music()
                        gesture = "pause"

                # Right-point (index extended, others folded) = Next
                elif index[0] > thumb[0] and middle[1] > index[1]:
                    if gesture != "next":
                        next_track()
                        gesture = "next"

                # Left-point = Previous
                elif index[0] < thumb[0] and middle[1] > index[1]:
                    if gesture != "prev":
                        previous_track()
                        gesture = "prev"

                # Two fingers up = Volume up
                elif index[1] < thumb[1] and middle[1] < thumb[1]:
                    if gesture != "vol_up":
                        volume_up()
                        gesture = "vol_up"

                # Thumb and pinky up = Volume down
                elif thumb[1] < index[1] and pinky[1] < index[1]:
                    if gesture != "vol_down":
                        volume_down()
                        gesture = "vol_down"

    # FPS display
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    cv2.putText(img, f'FPS: {int(fps)}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Hand Gesture Music Controller", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import pyautogui
import time
import math

# Setup MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

# Cooldown
gesture_cooldown = 1
last_gesture_time = time.time()
current_gesture = ""

# Distance calculator
def calc_distance(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

# Helpers
def is_extended(tip_id, pip_id, lm):
    return lm[tip_id].y < lm[pip_id].y

def all_folded(lm):
    return (
        lm[8].y > lm[6].y and
        lm[12].y > lm[10].y and
        lm[16].y > lm[14].y and
        lm[20].y > lm[18].y
    )

def all_extended(lm):
    return (
        is_extended(8, 6, lm) and
        is_extended(12, 10, lm) and
        is_extended(16, 14, lm) and
        is_extended(20, 18, lm)
    )

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    h, w, _ = frame.shape
    current_time = time.time()

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            lm = hand_landmarks.landmark

            gesture = None

            if current_time - last_gesture_time > gesture_cooldown:
                thumb_tip = lm[4]
                index_tip = lm[8]
                middle_tip = lm[12]
                ring_tip = lm[16]
                pinky_tip = lm[20]

                # ✊ Fist
                if all_folded(lm):
                    pyautogui.press('down')
                    gesture = "SLIDE"

                # ☝️ Index only
                elif (
                    is_extended(8, 6, lm) and
                    not is_extended(12, 10, lm) and
                    not is_extended(16, 14, lm) and
                    not is_extended(20, 18, lm)
                ):
                    pyautogui.press('up')
                    gesture = "JUMP"

                # ✌️ Peace sign
                elif (
                    is_extended(8, 6, lm) and
                    is_extended(12, 10, lm) and
                    not is_extended(16, 14, lm) and
                    not is_extended(20, 18, lm)
                ):
                    pyautogui.press('right')
                    gesture = "MOVE RIGHT"

                # 👌 OK sign
                elif (
                    calc_distance(thumb_tip, index_tip) < 0.05 and
                    is_extended(12, 10, lm) and
                    is_extended(16, 14, lm) and
                    is_extended(20, 18, lm)
                ):
                    pyautogui.press('left')
                    gesture = "MOVE LEFT"

                # ✋ Open hand
                elif all_extended(lm):
                    gesture = "IDLE"

                if gesture:
                    current_gesture = gesture
                    last_gesture_time = current_time
                    print(f"Gesture Detected: {gesture}")

    # Show current gesture
    if current_gesture:
        cv2.putText(frame, f"Gesture: {current_gesture}", (30, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("🕹️ Gesture Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

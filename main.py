import cv2
import mediapipe as mp
import pyautogui
import pickle
import time

import state
import settings

from voice import start_voice
from face_login import face_login
from database import log_event

# -------- SETTINGS --------
pyautogui.FAILSAFE = False

model = pickle.load(open("model.pkl", "rb"))

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

SCREEN_W, SCREEN_H = pyautogui.size()

prev_x, prev_y = 0, 0
last_click = 0
dragging = False

# -------- MAIN FUNCTION --------
def main():
    global prev_x, prev_y, last_click, dragging

    print("🔐 Starting Face Login...")
    face_login()

    print("🎤 Starting Voice Assistant...")
    start_voice()

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w, _ = frame.shape
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:

                # -------- CREATE FEATURE VECTOR --------
                sample = []
                for lm in hand.landmark:
                    sample.extend([lm.x, lm.y])

                pred = model.predict([sample])[0]

                # -------- INDEX FINGER --------
                ix = int(hand.landmark[8].x * w)
                iy = int(hand.landmark[8].y * h)

                # -------- MAP TO SCREEN --------
                sx = ix * SCREEN_W / w
                sy = iy * SCREEN_H / h

                # -------- SMOOTH MOVEMENT --------
                cx = prev_x + (sx - prev_x) / settings.SMOOTHING
                cy = prev_y + (sy - prev_y) / settings.SMOOTHING

                if state.assistant_active:
                    pyautogui.moveTo(cx, cy)

                prev_x, prev_y = cx, cy

                # -------- GESTURE ACTIONS --------
                current_time = time.time()

                if pred == "click" and current_time - last_click > settings.CLICK_DELAY:
                    pyautogui.click()
                    last_click = current_time

                elif pred == "right_click":
                    pyautogui.rightClick()

                elif pred == "double_click":
                    pyautogui.doubleClick()

                elif pred == "scroll_up":
                    pyautogui.scroll(100)

                elif pred == "scroll_down":
                    pyautogui.scroll(-100)

                elif pred == "drag":
                    if not dragging:
                        pyautogui.mouseDown()
                        dragging = True

                else:
                    if dragging:
                        pyautogui.mouseUp()
                        dragging = False

                if pred == "zoom_in":
                    pyautogui.hotkey("ctrl", "+")

                elif pred == "zoom_out":
                    pyautogui.hotkey("ctrl", "-")

                elif pred == "screenshot":
                    pyautogui.screenshot("screen.png")

                elif pred == "volume_up":
                    pyautogui.press("volumeup")

                elif pred == "volume_down":
                    pyautogui.press("volumedown")

                elif pred == "next_tab":
                    pyautogui.hotkey("ctrl", "tab")

                elif pred == "previous_tab":
                    pyautogui.hotkey("ctrl", "shift", "tab")

                elif pred == "pause":
                    state.assistant_active = False

                # -------- LOG --------
                log_event(pred)

                # -------- DISPLAY --------
                cv2.putText(frame, f"Gesture: {pred}", (10, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # -------- VOICE CLICK --------
        if state.click_trigger:
            pyautogui.click()
            state.click_trigger = False

        cv2.imshow("ASIS FINAL SYSTEM", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


# -------- RUN --------
if __name__ == "__main__":
    main()
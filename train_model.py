import cv2, mediapipe as mp, pickle
from sklearn.neighbors import KNeighborsClassifier

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

data, labels = [], []

def collect(label):
    cap = cv2.VideoCapture(0)
    count = 0

    print("Show:", label)

    while count < 60:
        ret, frame = cap.read()
        frame = cv2.flip(frame,1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        res = hands.process(rgb)

        if res.multi_hand_landmarks:
            for hand in res.multi_hand_landmarks:
                sample=[]
                for lm in hand.landmark:
                    sample.extend([lm.x,lm.y])

                data.append(sample)
                labels.append(label)
                count+=1

        cv2.imshow("Train",frame)
        if cv2.waitKey(1)==27: break

    cap.release()
    cv2.destroyAllWindows()

gestures = [
    "move",
    "click",
    "right_click",
    "double_click",
    "scroll_up",
    "scroll_down",
    "drag",
    "zoom_in",
    "zoom_out",
    "pause",
    "screenshot",
    "volume_up",
    "volume_down",
    "next_tab",
    "previous_tab"
]

for g in gestures:
    collect(g)

model = KNeighborsClassifier()
model.fit(data, labels)

pickle.dump(model, open("model.pkl","wb"))
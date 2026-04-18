import cv2

def face_login():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        cv2.putText(frame, "Press L to Login",
                    (50,50), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

        cv2.imshow("Face Login", frame)

        if cv2.waitKey(1) == ord('l'):
            break

    cap.release()
    cv2.destroyAllWindows()
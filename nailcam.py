import cv2
import time

from app.notifier import notify
from app.tracker import BiteTracker
from app.detector import Detector

detector = Detector()

cap = cv2.VideoCapture(0)
tracker = BiteTracker()

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)

    results = detector.process(frame)
    hand_landmarks = results["hands"]
    face_landmarks = results["faces"]

    if tracker.check_for_bite(face_landmarks, hand_landmarks, time.time()):
        notify("Stop Biting!", "Hands off your face 🚫")

    cv2.imshow('NailCam Watcher - Press Q to Quit', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

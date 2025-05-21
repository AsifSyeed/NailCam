import cv2
import mediapipe as mp
import time

from app.notifier import notify
from app.tracker import BiteTracker

mp_hands = mp.solutions.hands
mp_face_mesh = mp.solutions.face_mesh
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
face_mesh = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)
tracker = BiteTracker()

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    hand_results = hands.process(rgb_frame)
    face_results = face_mesh.process(rgb_frame)

    hand_landmarks = hand_results.multi_hand_landmarks or []
    face_landmarks = face_results.multi_face_landmarks or []

    if tracker.check_for_bite(face_landmarks, hand_landmarks, time.time()):
        notify("Stop Biting!", "Hands off your face 🚫")

    cv2.imshow('NailCam Watcher - Press Q to Quit', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

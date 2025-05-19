import cv2
import mediapipe as mp
import os
import math
import time

from Foundation import NSObject, NSUserNotification, NSUserNotificationCenter

def notify_mac(title, message):
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setInformativeText_(message)
    notification.setSoundName_("NSUserNotificationDefaultSoundName")
    NSUserNotificationCenter.defaultUserNotificationCenter().deliverNotification_(notification)

mp_hands = mp.solutions.hands
mp_face_mesh = mp.solutions.face_mesh
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
face_mesh = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

def euclidean_distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

last_alert_time = 0
cooldown_seconds = 10

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    hand_results = hands.process(rgb_frame)
    face_results = face_mesh.process(rgb_frame)

    if hand_results.multi_hand_landmarks and face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:
            upper_lip = face_landmarks.landmark[13]
            for hand_landmarks in hand_results.multi_hand_landmarks:
                for tip_index in [4, 8, 12, 16, 20]:
                    fingertip = hand_landmarks.landmark[tip_index]
                    distance = euclidean_distance(fingertip, upper_lip)

                    if distance < 0.07:
                        current_time = time.time()
                        if current_time - last_alert_time > cooldown_seconds:
                            notify_mac("Stop Biting!", "Hands off your face 🚫")
                            last_alert_time = current_time
                        break

    cv2.imshow('NailCam Watcher - Press Q to Quit', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

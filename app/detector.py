# app/detector.py

import cv2
import mediapipe as mp

class Detector:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
        self.face_mesh = mp.solutions.face_mesh.FaceMesh()

    def process(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        hand_results = self.hands.process(rgb_frame)
        face_results = self.face_mesh.process(rgb_frame)
        return {
            "hands": hand_results.multi_hand_landmarks or [],
            "faces": face_results.multi_face_landmarks or []
        }

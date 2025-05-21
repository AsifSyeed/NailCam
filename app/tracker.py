import math

class BiteTracker:
    def __init__(self, threshold=0.07, cooldown=10):
        self.threshold = threshold
        self.cooldown = cooldown
        self.last_alert_time = 0

    def euclidean_distance(self, p1, p2):
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def check_for_bite(self, face_landmarks_list, hand_landmarks_list, current_time):
        if not face_landmarks_list or not hand_landmarks_list:
            return False

        face_landmarks = face_landmarks_list[0]
        if not hasattr(face_landmarks, "landmark") or len(face_landmarks.landmark) <= 13:
            return False

        upper_lip = face_landmarks.landmark[13]

        for hand_landmarks in hand_landmarks_list:
            if not hasattr(hand_landmarks, "landmark"):
                continue
            for tip_index in [4, 8, 12, 16, 20]:
                if tip_index >= len(hand_landmarks.landmark):
                    continue
                fingertip = hand_landmarks.landmark[tip_index]
                distance = self.euclidean_distance(fingertip, upper_lip)
                if distance < self.threshold:
                    if current_time - self.last_alert_time > self.cooldown:
                        self.last_alert_time = current_time
                        return True
        return False

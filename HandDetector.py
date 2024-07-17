import cv2
import numpy as np
import mediapipe as mp
import pyautogui as pg

class HandDetector:
    
    def __init__(self, max_hands=2, detection_conf=0.5, tracking_conf=0.5):
        self.hand = mp.solutions.hands.Hands()
        self._drawing_utils = mp.solutions.drawing_utils
        self.hand_landmarks = self._create_hand_landmarks()

    def _create_hand_landmarks(self) -> dict:
        hand_landmarks = dict()
        fingers = ['thumb', 'index', 'middle', 'ring', 'pinkie']
        for finger in fingers:
            hand_landmarks[finger] = {
                'x': 0,
                'y': 0
            }
        return hand_landmarks
        
    def detect_hands(self, frame: np.ndarray) -> None:
        height, width, _ = frame.shape
        s_height, s_width = pg.size()
        detection = self.hand.process(frame)
        hands = detection.multi_hand_landmarks
        if hands:
            for hand in hands:
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * width)
                    y = int(landmark.y * height)
                    if id == 12:
                        # cv2.circle(frame, (x, y), 10, (0, 255, 255))
                        finger = self.hand_landmarks['index']
                        finger['x'] = s_width / width * x
                        finger['y'] = s_height / height * y
                        pg.moveTo(finger['x'], finger['y'])
                    if id == 8:
                        # cv2.circle(frame, (x, y), 10, (0, 255, 255))
                        finger = self.hand_landmarks['thumb']
                        finger['x'] = s_width / width * x
                        finger['y'] = s_height / height * y
                        if abs(self.hand_landmarks['index']['y'] - finger['y']) < 10:
                            pg.click()
                self._drawing_utils.draw_landmarks(frame, hand)
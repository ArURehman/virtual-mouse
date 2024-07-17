import cv2
from HandDetector import HandDetector

def main():
    cam = cv2.VideoCapture(0)
    hand_detector = HandDetector()
    while True:
        ret, frame = cam.read()
        assert ret == True
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        hand_detector.detect_hands(rgb_frame)
        cv2.imshow('', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
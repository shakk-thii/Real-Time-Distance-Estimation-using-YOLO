import cv2
import time
from core.detector import ObjectDetector

def main():
    print("=" * 50)
    print("  Real-Time Distance Estimation System")
    print("  Press Q to quit")
    print("=" * 50)

    detector = ObjectDetector(confidence=0.5)
    cap      = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[Error] Could not open webcam.")
        return

    prev_time = time.time()
    print("[System] Webcam opened. Starting detection...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[Error] Failed to read frame.")
            break

        detections  = detector.detect(frame)
        frame       = detector.draw(frame, detections)

        curr_time   = time.time()
        fps         = 1 / (curr_time - prev_time)
        prev_time   = curr_time

        cv2.putText(
            frame,
            f"FPS: {int(fps)}  Objects: {len(detections)}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8, (255, 255, 255), 2
        )

        cv2.imshow("Real-Time Distance Estimator — Press Q to quit", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[System] Stopped.")

if __name__ == "__main__":
    main()
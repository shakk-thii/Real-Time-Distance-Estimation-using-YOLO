import cv2
import numpy as np
from ultralytics import YOLO
from core.distance import calculate_distance, distance_to_color

class ObjectDetector:
    def __init__(self, model_path: str = "yolov8n.pt", confidence: float = 0.5):
        print("[Detector] Loading YOLOv8 model...")
        self.model      = YOLO(model_path)
        self.confidence = confidence
        print("[Detector] Model loaded successfully.")

    def detect(self, frame: np.ndarray) -> list:
        results    = self.model(frame, verbose=False)[0]
        detections = []

        for box in results.boxes:
            confidence = float(box.conf[0])
            if confidence < self.confidence:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            pixel_width     = x2 - x1
            class_id        = int(box.cls[0])
            label           = self.model.names[class_id]
            distance        = calculate_distance(label, pixel_width)

            detections.append({
                "label"     : label,
                "confidence": round(confidence, 2),
                "box"       : (x1, y1, x2, y2),
                "distance"  : distance,
            })

        return detections

    def draw(self, frame: np.ndarray, detections: list) -> np.ndarray:
        for det in detections:
            x1, y1, x2, y2 = det["box"]
            label           = det["label"]
            confidence      = det["confidence"]
            distance        = det["distance"]
            color           = distance_to_color(distance)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            text = f"{label} | {distance}m | {int(confidence*100)}%"

            (text_w, text_h), _ = cv2.getTextSize(
                text, cv2.FONT_HERSHEY_SIMPLEX, 0.55, 2
            )
            cv2.rectangle(
                frame,
                (x1, y1 - text_h - 8),
                (x1 + text_w, y1),
                color, -1
            )
            cv2.putText(
                frame, text,
                (x1, y1 - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (255, 255, 255), 2
            )

        return frame
import cv2
import mediapipe as mp

def get_direction(stop_event, tilt):
    # Setup
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils
    mp_detection = mp.solutions.face_detection

    cap = cv2.VideoCapture(0)

    # Initialize face detector
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        while cap.isOpened() and not stop_event.is_set():
            success, frame = cap.read()
            if not success:
                break

            # Convert to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_detection.process(image)

            # Draw detections
            if results.detections:
                for detection in results.detections:
                    left_eye = mp_detection.get_key_point(detection, key_point_enum=0)
                    right_eye = mp_detection.get_key_point(detection, key_point_enum=1)
                    if right_eye.y == left_eye.y:
                        tilt['Val'] = 1
                    slope = (right_eye.y-left_eye.y) / (right_eye.x-left_eye.x)
                    if slope > 0.2:
                        tilt['Val'] = -1 # left
                    elif slope < -0.2:
                        tilt['Val'] = 1 # right
                    else:
                        tilt['Val'] = 0
    if cap is not None:
        cap.release()
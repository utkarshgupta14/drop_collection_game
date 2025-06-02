import cv2
import mediapipe as mp

def get_direction(show_video=False):
    # Setup
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils
    mp_detection = mp.solutions.face_detection

    # Initialize face detector
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
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
                        print("VERTICAL FACE BRUHH")
                        exit()
                    slope = (right_eye.y-left_eye.y) / (right_eye.x-left_eye.x)
                    if slope > 0.7:
                        tilt = -1
                    elif slope < -0.7:
                        tilt = 1
                    else:
                        tilt = None
                    
                    if show_video == True:
                        if slope > 0.2:
                            print("LEFT TILT")
                        elif slope < -0.2:
                            print("RIGHT TILT")
                        else:
                            print("NEUTRAL")
                        mp_drawing.draw_detection(frame, detection)

            if show_video:
                cv2.imshow('MediaPipe Face Detection', frame)
                if cv2.waitKey(5) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    get_direction(True)
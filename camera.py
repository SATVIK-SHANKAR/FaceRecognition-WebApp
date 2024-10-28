# import cv2
# import numpy as np

# class VideoCamera:
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         self.face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_alt.xml')

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         success, frame = self.video.read()
#         if not success:
#             return None
        
#         ret, jpeg = cv2.imencode('.jpg', frame)
#         return jpeg.tobytes()

#     def get_face_frame(self):
#         success, frame = self.video.read()
#         if not success:
#             return None, None

#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
#         if len(faces) == 0:
#             return None, None

#         x, y, w, h = faces[0]
#         offset = 5
#         face_section = frame[y-offset:y+h+offset, x-offset:x+w+offset]
#         face_section = cv2.resize(face_section, (100, 100))
        
#         return face_section, frame



import cv2
import numpy as np

class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_alt.xml')
        # Set resolution to 640x480
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, frame = self.video.read()
        if not success:
            return None
        
        # Detect faces and draw rectangle
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def get_face_frame(self):
        success, frame = self.video.read()
        if not success:
            return None, None

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if len(faces) == 0:
            return None, frame

        # Get the largest face
        face = max(faces, key=lambda x: x[2] * x[3])
        x, y, w, h = face
        
        offset = 10
        y1 = max(y - offset, 0)
        y2 = min(y + h + offset, frame.shape[0])
        x1 = max(x - offset, 0)
        x2 = min(x + w + offset, frame.shape[1])
        
        face_section = frame[y1:y2, x1:x2]
        if face_section.size == 0:
            return None, frame
            
        face_section = cv2.resize(face_section, (100, 100))
        return face_section, frame
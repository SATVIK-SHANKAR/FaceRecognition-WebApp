# from flask import Flask, render_template, Response, jsonify, request
# import cv2
# import numpy as np
# import os
# from camera import VideoCamera
# from face_utils import FaceUtils

# app = Flask(__name__)
# video_camera = None
# face_utils = FaceUtils()

# @app.route('/')
# def index():
#     return render_template('index.html')

# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# @app.route('/video_feed')
# def video_feed():
#     global video_camera
#     if video_camera is None:
#         video_camera = VideoCamera()
#     return Response(gen(video_camera),
#                    mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/register', methods=['POST'])
# def register():
#     name = request.form.get('name')
#     if face_utils.check_existing_user(name):
#         return jsonify({'status': 'error', 'message': 'User already registered'})
    
#     global video_camera
#     if video_camera is None:
#         video_camera = VideoCamera()
    
#     success = face_utils.register_face(video_camera, name)
#     if success:
#         return jsonify({'status': 'success', 'message': 'Registration successful'})
#     return jsonify({'status': 'error', 'message': 'Registration failed'})

# @app.route('/recognize', methods=['POST'])
# def recognize():
#     global video_camera
#     if video_camera is None:
#         video_camera = VideoCamera()
    
#     name = face_utils.recognize_face(video_camera)
#     if name:
#         return jsonify({'status': 'success', 'name': name})
#     return jsonify({'status': 'error', 'message': 'Face not recognized'})

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, Response, jsonify, request
import cv2
import numpy as np
import os
from camera import VideoCamera
from face_utils import FaceUtils

app = Flask(__name__)
video_camera = None
face_utils = FaceUtils()

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        if frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    global video_camera
    if video_camera is None:
        video_camera = VideoCamera()
    return Response(gen(video_camera),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    if not name:
        return jsonify({'status': 'error', 'message': 'Name is required'})
        
    if face_utils.check_existing_user(name):
        return jsonify({'status': 'error', 'message': 'User already registered'})
    
    global video_camera
    if video_camera is None:
        video_camera = VideoCamera()
    
    success = face_utils.register_face(video_camera, name)
    if success:
        return jsonify({'status': 'success', 'message': 'Registration successful! Face data captured.'})
    return jsonify({'status': 'error', 'message': 'Registration failed. Please ensure your face is clearly visible.'})

@app.route('/recognize', methods=['POST'])
def recognize():
    if len(os.listdir('face_dataset')) == 0:
        return jsonify({'status': 'error', 'message': 'No registered users. Please register first.'})
        
    global video_camera
    if video_camera is None:
        video_camera = VideoCamera()
    
    name = face_utils.recognize_face(video_camera)
    if name:
        return jsonify({'status': 'success', 'name': name})
    return jsonify({'status': 'error', 'message': 'Face not recognized or no face detected'})

if __name__ == '__main__':
    app.run(debug=True)
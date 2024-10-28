# import numpy as np
# import os
# import cv2

# class FaceUtils:
#     def __init__(self):
#         self.dataset_path = 'face_dataset'
#         self.face_data = []
#         self.labels = []
#         self.names = {}
#         self.load_dataset()

#     def load_dataset(self):
#         class_id = 0
#         for fx in os.listdir(self.dataset_path):
#             if fx.endswith('.npy'):
#                 self.names[class_id] = fx[:-4]
#                 data_item = np.load(os.path.join(self.dataset_path, fx))
#                 self.face_data.append(data_item)
#                 target = class_id * np.ones((data_item.shape[0],))
#                 class_id += 1
#                 self.labels.append(target)

#         if self.face_data:
#             self.face_dataset = np.concatenate(self.face_data, axis=0)
#             self.face_labels = np.concatenate(self.labels, axis=0).reshape((-1, 1))
#             self.trainset = np.concatenate((self.face_dataset, self.face_labels), axis=1)

#     def check_existing_user(self, name):
#         return os.path.exists(os.path.join(self.dataset_path, f"{name}.npy"))

#     def register_face(self, camera, name):
#         face_data = []
#         for _ in range(50):  # Capture 50 frames
#             face_section, _ = camera.get_face_frame()
#             if face_section is not None:
#                 face_data.append(face_section)

#         if len(face_data) < 10:  # Minimum required faces
#             return False

#         face_data = np.array(face_data)
#         face_data = face_data.reshape((face_data.shape[0], -1))
#         file_path = os.path.join(self.dataset_path, f"{name}.npy")
#         np.save(file_path, face_data)
#         self.load_dataset()  # Reload dataset
#         return True

#     def recognize_face(self, camera):
#         face_section, _ = camera.get_face_frame()
#         if face_section is None:
#             return None

#         # KNN Recognition
#         out = self.knn(self.trainset, face_section.flatten())
#         return self.names.get(int(out))

#     def distance(self, v1, v2):
#         return np.sqrt(((v1-v2)**2).sum())

#     def knn(self, train, test, k=5):
#         dist = []
#         for i in range(train.shape[0]):
#             ix = train[i, :-1]
#             iy = train[i, -1]
#             d = self.distance(test, ix)
#             dist.append([d, iy])
#         dk = sorted(dist, key=lambda x: x[0])[:k]
#         labels = np.array(dk)[:, -1]
#         output = np.unique(labels, return_counts=True)
#         index = np.argmax(output[1])
#         return output[0][index]




import numpy as np
import os
import cv2
import time

class FaceUtils:
    def __init__(self):
        self.dataset_path = 'face_dataset'
        self.face_data = []
        self.labels = []
        self.names = {}
        os.makedirs(self.dataset_path, exist_ok=True)
        self.load_dataset()

    def load_dataset(self):
        self.face_data = []
        self.labels = []
        self.names = {}
        class_id = 0
        
        for fx in os.listdir(self.dataset_path):
            if fx.endswith('.npy'):
                self.names[class_id] = fx[:-4]
                data_item = np.load(os.path.join(self.dataset_path, fx))
                self.face_data.append(data_item)
                target = class_id * np.ones((data_item.shape[0],))
                class_id += 1
                self.labels.append(target)

        if self.face_data:
            self.face_dataset = np.concatenate(self.face_data, axis=0)
            self.face_labels = np.concatenate(self.labels, axis=0).reshape((-1, 1))
            self.trainset = np.concatenate((self.face_dataset, self.face_labels), axis=1)

    def check_existing_user(self, name):
        return os.path.exists(os.path.join(self.dataset_path, f"{name}.npy"))

    def register_face(self, camera, name):
        face_data = []
        start_time = time.time()
        
        while len(face_data) < 20 and time.time() - start_time < 10:  # 10 second timeout
            face_section, _ = camera.get_face_frame()
            if face_section is not None:
                face_data.append(face_section.flatten())
                time.sleep(0.2)  # Add small delay between captures

        if len(face_data) < 10:  # Minimum required faces
            return False

        face_data = np.array(face_data)
        file_path = os.path.join(self.dataset_path, f"{name}.npy")
        np.save(file_path, face_data)
        self.load_dataset()  # Reload dataset
        return True

    def recognize_face(self, camera):
        if not hasattr(self, 'trainset'):
            return None
            
        face_section, _ = camera.get_face_frame()
        if face_section is None:
            return None

        try:
            flattened_face = face_section.flatten()
            out = self.knn(self.trainset, flattened_face)
            return self.names.get(int(out))
        except Exception as e:
            print(f"Recognition error: {e}")
            return None

    def distance(self, v1, v2):
        return np.sqrt(((v1-v2)**2).sum())

    def knn(self, train, test, k=5):
        if len(train) == 0:
            return None
            
        dist = []
        for i in range(train.shape[0]):
            ix = train[i, :-1]
            iy = train[i, -1]
            d = self.distance(test, ix)
            dist.append([d, iy])
        
        dk = sorted(dist, key=lambda x: x[0])[:k]
        labels = np.array(dk)[:, -1]
        output = np.unique(labels, return_counts=True)
        index = np.argmax(output[1])
        return output[0][index]
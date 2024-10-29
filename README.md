# Real-Time Face Recognition Web App

## Overview
This project is a real-time face recognition web application built using Flask, OpenCV, and K-Nearest Neighbors (KNN) for accurate face recognition. It captures video frames from a webcam, detects faces using the Haar Cascade Classifier, collects face data for registration, and performs face recognition in real-time. Users can register new faces and recognize registered faces directly through the web interface.

## Project Structure
The structure of this web-based project is as follows:

- **static/css/style.css**: Styles for the web UI, including layout and aesthetic improvements.
- **static/js/main.js**: Contains JavaScript functions for registering and recognizing faces with real-time feedback.
- **templates/base.html** and **index.html**: HTML templates for the web interface, using Jinja for rendering dynamic content.
- **app.py**: Flask application to handle routing, video feed, and face recognition functions.
- **camera.py**: Captures video from the webcam and detects faces using the Haar Cascade Classifier.
- **face_utils.py**: Manages face data registration, saving, loading, and recognition using KNN.
- **face_dataset/**: Directory where face data is stored as `.npy` files for registered users.
- **models/haarcascade_frontalface_alt.xml**: Haar Cascade model file for face detection.

## Setup and Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/real-time-face-recognition-webapp.git
   cd real-time-face-recognition-webapp

## Setup and Installation

2. **Install Dependencies:** Ensure Python is installed, then install the required libraries.

    ```bash
    pip install -r requirements.txt
    ```

3. **Download Haar Cascade Classifier:** Download the `haarcascade_frontalface_alt.xml` file if not already present and place it in the `models` directory.

## Running the Project

1. **Start the Flask App:**

    ```bash
    python app.py
    ```

2. **Access the Web App:** Open your web browser and go to `http://127.0.0.1:5000`.

3. **Register a New User:** Enter a name in the input field, click **Register New User**, and allow the app to capture face data for registration.

4. **Recognize Face:** Click **Recognize Face** to identify registered users in real-time.

## Prototype

Below is a screenshot of the Face Recognition System web app prototype.

![Face Recognition System Prototype](https://github.com/SATVIK-SHANKAR/FaceRecognition-WebApp/blob/main/WebAppTest.jpeg?raw=true)

This interface allows users to register their faces by entering their name and recognizing faces in real-time. The detected faces are highlighted with a green box.

## Key Concepts and Theory

### Haar Cascade Classifier
This method uses positive and negative images to train the model to recognize faces with high accuracy. It’s particularly effective for face detection and performs efficiently in real-time applications.

### K-Nearest Neighbors (KNN)
KNN is used to classify faces based on the `k` nearest neighbors from the stored face dataset. Its simplicity and interpretability make it suitable for this face recognition application.

## Applications

- **Security Systems**: Real-time face recognition for improved security.
- **User Authentication**: Secure device unlocking or identity verification.
- **Personalized User Experience**: Enhances services with user recognition.

## Advantages

- **Real-Time Processing**: Provides immediate face detection and recognition.
- **High Accuracy**: Reliable face recognition based on trained datasets.
- **Scalability**: Supports multiple users in the dataset for recognition.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For questions or collaboration, reach out to **Satvik Shankar** at [satvik.shankar2003@gmail.com](mailto:satvik.shankar2003@gmail.com).

**GitHub Repository**: [Original Project](https://github.com/SATVIK-SHANKAR/FaceRecognition)

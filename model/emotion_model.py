import cv2
import numpy as np
from tensorflow.keras.models import load_model

class EmotionRecognizer:
    def __init__(self, model_path="model/emotion_model.h5"):
        self.model = load_model(model_path)
        self.emotion_labels = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

    def preprocess(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = cv2.resize(gray, (48, 48))
        face = face.astype("float32") / 255.0
        face = np.expand_dims(face, axis=0)
        face = np.expand_dims(face, axis=-1)
        return face

    def predict(self, frame):
        face = self.preprocess(frame)
        preds = self.model.predict(face)[0]
        emotion_idx = np.argmax(preds)
        emotion = self.emotion_labels[emotion_idx]
        confidence = float(preds[emotion_idx])
        return emotion, confidence
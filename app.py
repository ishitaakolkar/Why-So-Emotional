import streamlit as st
from model.emotion_model import EmotionRecognizer
from utils.video_utils import get_video_frame, get_uploaded_image
from utils.ui_utils import display_dashboard
import cv2

st.set_page_config(page_title="Real-Time Emotion Recognition", layout="centered", page_icon=":smiley:")
st.title("Real-Time Emotion Recognition :smiley:")
st.markdown("""
Welcome to the interactive emotion recognition app!  
Detect emotions from your webcam or uploaded images in real time.  
Enjoy dynamic dashboards, emoji overlays, custom mood responses, and animated visuals!
""")

input_mode = st.sidebar.radio("Choose Input Mode:", ("Webcam", "Image Upload"))
emotion_recognizer = EmotionRecognizer()

if input_mode == "Webcam":
    st.info("Starting live webcam feed... (use Chrome/Edge for best support)")
    frame = get_video_frame()
elif input_mode == "Image Upload":
    uploaded_img = st.file_uploader("Upload an image for emotion detection", type=["jpg", "jpeg", "png"])
    frame = get_uploaded_image(uploaded_img)
else:
    frame = None

if frame is not None:
    emotion, confidence = emotion_recognizer.predict(frame)
    display_dashboard(frame, emotion, confidence)
else:
    st.warning("No input detected. Please enable your webcam or upload an image.")

st.markdown("---")
st.markdown("Made with :heart: using Streamlit & Deep Learning | [GitHub Repo](https://github.com/ishitaakolkar/emotion-recognition-streamlit)")
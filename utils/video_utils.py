import streamlit as st
import cv2
import numpy as np

def get_video_frame():
    video_frame = st.camera_input("Capture emotion from webcam")
    if video_frame is not None:
        bytes_data = video_frame.getvalue()
        img_array = np.frombuffer(bytes_data, np.uint8)
        frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        return frame
    return None

def get_uploaded_image(uploaded_img):
    if uploaded_img is not None:
        bytes_data = uploaded_img.getvalue()
        img_array = np.frombuffer(bytes_data, np.uint8)
        frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        return frame
    return None
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import os

# Custom theme
def set_custom_theme():
    custom_css = """
    <style>
    body { background-color: #f5f7fa; }
    .stApp { font-family: 'Roboto', sans-serif; }
    .emoji { font-size: 48px; animation: pulse 1.2s infinite; }
    @keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.1); } 100% { transform: scale(1); } }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Emoji overlay mapping
EMOJI_MAP = {
    "Angry": "assets/emojis/angry.png",
    "Disgust": "assets/emojis/disgust.png",
    "Fear": "assets/emojis/fear.png",
    "Happy": "assets/emojis/happy.png",
    "Sad": "assets/emojis/sad.png",
    "Surprise": "assets/emojis/surprise.png",
    "Neutral": "assets/emojis/neutral.png",
}

# Live dashboard: emotion, confidence graph, timeline, emoji
def display_dashboard(frame, emotion, confidence):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image(frame, channels="BGR", caption="Live Feed", use_column_width=True)
        st.markdown(f"<div class='emoji'><img src='{EMOJI_MAP[emotion]}' width=48 /></div>", unsafe_allow_html=True)
        st.subheader(f"Detected Emotion: **{emotion}**")
    with col2:
        st.metric("Confidence", f"{confidence*100:.1f}%")
        st.progress(confidence)
        # Timeline placeholder (expand for persistent history)
        st.write("Emotion History Timeline (last 5)")
        st.line_chart([confidence])  # Replace with full history in expanded version
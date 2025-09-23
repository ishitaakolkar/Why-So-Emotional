import streamlit as st
import os
from PIL import Image
from utils.mood_responses import get_mood_response

# Emoji mapping
EMOJI_MAP = {
    "Angry": "assets/emojis/angry.png",
    "Disgust": "assets/emojis/disgust.png",
    "Fear": "assets/emojis/fear.png",
    "Happy": "assets/emojis/happy.png",
    "Sad": "assets/emojis/sad.png",
    "Surprise": "assets/emojis/surprise.png",
    "Neutral": "assets/emojis/neutral.png",
}

EMOTION_COLORS = {
    "Happy": "#eaffea",
    "Sad": "#eaf2ff",
    "Angry": "#ffeaea",
    "Fear": "#fffbe6",
    "Surprise": "#e6f7ff",
    "Neutral": "#f5f5f5"
}

ANIMATION_MAP = {
    "Happy": "sparkle",
    "Sad": "calm",
    # Extend for other emotions if desired
}

def set_custom_theme(emotion=None):
    # Dynamically set background color based on emotion
    color = EMOTION_COLORS.get(emotion, "#f5f5f5")
    st.markdown(
        f"""<style>
        .stApp {{ background-color: {color}; transition: background-color 1s; font-family: 'Roboto', sans-serif; }}
        </style>""",
        unsafe_allow_html=True,
    )
    st.markdown('<link rel="stylesheet" href="static/custom.css">', unsafe_allow_html=True)

def show_animation(emotion):
    anim_class = ANIMATION_MAP.get(emotion)
    if anim_class:
        st.markdown(f'<div class="{anim_class}"></div>', unsafe_allow_html=True)

def display_dashboard(frame, emotion, confidence):
    set_custom_theme(emotion)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image(frame, channels="BGR", caption="Live Feed", use_column_width=True)
        st.markdown(
            f"<div class='emoji-anim'><img src='{EMOJI_MAP[emotion]}' width=120 /></div>",
            unsafe_allow_html=True,
        )
        st.subheader(f"Detected Emotion: **{emotion}** <span style='font-size:18px;'>({confidence*100:.1f}%)</span>", unsafe_allow_html=True)
        show_animation(emotion)
    with col2:
        st.metric("Confidence", f"{confidence*100:.1f}%")
        st.progress(confidence)
        st.markdown(f"**Mood Response:**<br><i>{get_mood_response(emotion)}</i>", unsafe_allow_html=True)
        st.write("Emotion History Timeline (last 5)")
        st.line_chart([confidence])
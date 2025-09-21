import random

EMOTION_RESPONSES = {
    "Happy": ["You're amazing! Keep smiling 😄"],
    "Sad": [
        "Tough times don't last, but tough people do 💪",
        "Every day may not be good, but there's something good in every day."
    ],
    "Angry": [
        "Take a deep breath, everything will be okay 🌿",
        "Pause. Breathe. Reset."
    ],
    "Fear": ["It's okay, you are in control. Breathe deeply."],
    "Surprise": ["Whoa! Didn't expect that, huh? 😲"],
    "Neutral": ["Just another day, let's make the most of it!"]
}

EMOTION_EMOJIS = {
    "Happy": "😄",
    "Sad": "😢",
    "Angry": "😠",
    "Fear": "😨",
    "Surprise": "😲",
    "Neutral": "😐"
}

def detect_emotion(img):
    # Load your pre-trained model and predict here
    # For demonstration, return random emotion and confidence
    emotions = list(EMOTION_RESPONSES.keys())
    emotion = random.choice(emotions)
    confidence = random.uniform(0.75, 1.0)
    return emotion, confidence

def get_mood_response(emotion):
    responses = EMOTION_RESPONSES.get(emotion, ["Have a great day!"])
    return random.choice(responses)

def get_emoji(emotion):
    return f"<span style='font-size:72px'>{EMOTION_EMOJIS.get(emotion, '🙂')}</span>"
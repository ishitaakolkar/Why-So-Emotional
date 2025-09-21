# Real-Time Emotion Recognition Web App 😃

A fun, interactive, and professional-quality AI application to recognize emotions from facial expressions in real-time or from images — built with Python, Streamlit, and deep learning!

![Demo GIF](assets/demo.gif)

---

## 🚀 Features

- **Live Webcam Feed**: Real-time emotion detection using your webcam.
- **Image Upload**: Fallback option to upload images for emotion analysis.
- **Deep Learning Model**: Uses MobileNet/FER2013 for accurate emotion recognition.
- **Dynamic Dashboard**: See detected emotion, live confidence graph, emoji overlays, and emotion timeline.
- **Polished UI/UX**: Custom color themes, subtle animations, and a clean, professional layout.
- **Beginner-Friendly Code**: Modular, readable, well-commented, and ready for collaboration!

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/ishitaakolkar/emotion-recognition-streamlit.git
   cd emotion-recognition-streamlit
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download pre-trained model**
   - Place `emotion_model.h5` (MobileNet/FER2013) in the `model/` folder.
   - [Get model weights here](https://github.com/oarriaga/face_classification) or use your own.

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 🤖 Model Explanation

- **Architecture**: Lightweight CNN or MobileNet transfer learning, trained on FER2013 dataset.
- **Input**: 48x48 grayscale face images.
- **Output**: Emotion probabilities — Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral.

---

## 📸 Screenshots

![Screenshot](assets/screenshots/demo_ui.png)
![Dashboard](assets/screenshots/dashboard.png)

---

## 👥 Contribution Guidelines

- Fork the repo and create a pull request for improvements.
- Please document your code and add clear commit messages.
- Check issues for ideas or bugs to fix!

---

## 📄 License

MIT License

---

**Made with ❤️ by Ishita Akolkar (https://github.com/ishitaakolkar)**
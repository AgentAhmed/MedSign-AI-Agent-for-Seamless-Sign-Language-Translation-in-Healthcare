import streamlit as st
import cv2
from advanced_sign_model import AdvancedSignRecognizer
from llama_translation import ModelTranslator
from upstage_context import MedicalContextualizer
from utils import text_to_speech_offline  # Offline TTS
from PIL import Image

# Initialize components
sign_recognizer = AdvancedSignRecognizer()
translator = ModelTranslator()
upstage_api_key = "up_VcBniTeOjMk76acpRAqHUMyrvh9tK"  # Replace with your Upstage API key
medical_contextualizer = MedicalContextualizer(api_key=upstage_api_key)

st.title("Universal AI Sign Language Translator with Offline TTS")

run_camera = st.checkbox("Turn On Camera")

if run_camera:
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture video")
            break
        
        recognized_sign = sign_recognizer.recognize_sign(frame)
        if recognized_sign:
            st.write(f"Recognized Sign: {recognized_sign}")

            # Medical translation using Upstage
            medical_translation = medical_contextualizer.query_upstage(recognized_sign)
            st.write(f"Medical Translation: {medical_translation}")

            # Multilingual translation using LLaMA 3.1
            translated_text = translator.translate_text(medical_translation)
            st.write(f"Translated Text: {translated_text}")

            # Convert recognized text to offline speech
            text_to_speech_offline(translated_text)  # Offline TTS
        
        # Display the video frame in Streamlit
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        st.image(img)

        if st.button("Stop Camera", key="E"):
            break
    cap.release()

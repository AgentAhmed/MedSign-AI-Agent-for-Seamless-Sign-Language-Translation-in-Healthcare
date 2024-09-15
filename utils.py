import pyttsx3

# Offline Text-to-Speech using pyttsx3
def text_to_speech_offline(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

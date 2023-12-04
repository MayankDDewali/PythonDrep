# pip install speechrecognition
# pip install wikipedia
# pip install openai

import speech_recognition as sr
import pyttsx3              # This library is for speaking

# This function is for voice
def speek(text):
    voice = pyttsx3.init()
    voice.say(text)
    voice.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}")

print("Pycarm")
speek("Hello I am Jarvis")
print("Listening...")
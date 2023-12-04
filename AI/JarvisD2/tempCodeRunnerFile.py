def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {querry}")

print("Pycarm")
speek("Hello I am Jarvis")
print("Listening...")
# text = takeCommand()
# speek(text)
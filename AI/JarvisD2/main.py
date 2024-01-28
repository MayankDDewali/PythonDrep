# Importing required libraries
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from AppOpener import open
import wikipedia

# Function for voice output
def speak(text):
    voice = pyttsx3.init()
    voice.say(text)
    voice.runAndWait()

# Function for voice input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Adjust the pause_threshold if needed
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Error:", e)
            return "Some Error Occurred. Sorry from my side."

# Introduction
# speak("Hello sir! What's your command?")
speak(f"What's your command, sir?")

while True:
    print("What's your command, sir?")
    text = takeCommand()

    # This is for opening websites
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
             ["google", "https://www.google.com"], ["github", "https://github.com/"]]

    # Opening the site in the list of lists
    for site in sites:
        if f"Open {site[0]}".lower() in text.lower():
            speak(f"Opening {site[0]}, sir...")
            webbrowser.open(site[1])

    # For getting the time
    if "the time".lower() in text:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {current_time}")

    # For opening applications
    apps = [["vs code", "Visual Studio Code"], ["whatsapp", "Whatsapp"], ["Dev C", "Dev-C++"],
            ["pycharm", "PyCharm Community Edition 2023.1.2"]]

    # Opening the app in the list of lists
    for app in apps:
        if f"Open {app[0]}".lower() in text.lower():
            speak(f"Opening {app[0]}, sir...")
            open(app[1])

    # For asking questions and retrieving answers from Wikipedia
    if "I have some questions".lower() in text.lower():
        speak("Alright! What's your question, sir...")
        question = takeCommand()
        speak(f"Your question is: {question}")
        print("Searching for the answer! Please Wait...")
        speak(f"Searching for the answer! Please Wait...")

        # Set the number of sentences you want in the answer
        num_sentences = 3

        try:
            result = wikipedia.summary(question, num_sentences)
            print(result)
            speak(result)
        except wikipedia.exceptions.PageError:
            print("Sorry, I couldn't find information for that topic.")
            speak("Sorry, I couldn't find information for that topic.")
        except Exception as e:
            print(f"An error occurred: {e}")
            speak("Sorry, an error occurred while fetching information.")

    # Adding extra questions
    if "Tell me about the founder of".lower() in text.lower():
        # speak("Of course")
        qqs = "Raj Bhatt, Founder of Elara Capital, a global investment bank, brings over three decades of expertise in executing innovative financial transactions. As a financial re-engineering and fundraising expert, he has successfully managed complex deals across seven locations on three continents. Raj Bhatt's stellar track record includes achievements in restructuring, mergers, acquisitions, and raising equity and debt in international markets. Since founding Elara in 2002, he serves as its Vice-Chairman & CEO, guiding its evolution into a capital markets powerhouse with diverse ventures in corporate advisory, asset management, broking, mergers & acquisitions, and private equity, spanning offices in India, New York, Singapore, Mauritius, and London."
        print(qqs)
        speak(f"{qqs}")
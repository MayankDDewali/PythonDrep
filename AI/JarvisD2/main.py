# Importing required libraries
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import requests
from AppOpener import open
from bs4 import BeautifulSoup

# Function for voice output
def speak(text):
    voice = pyttsx3.init()  # Initialize the text-to-speech engine
    voice.say(text)         # Queue the text to be spoken
    voice.runAndWait()      # Wait for the speech to finish before continuing

# Function for voice input
def takeCommand():
    r = sr.Recognizer()     # Initialize the recognizer
    with sr.Microphone() as source:
        # Adjust the pause_threshold if needed
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)    # Listen for audio input
        try:
            query = r.recognize_google(audio, language="en-in")  # Recognize the audio using Google Speech Recognition
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Error:", e)
            return "Some Error Occurred. Sorry from my side."

# Introduction
speak(f"What's your command, sir?")  # Greet the user

while True:
    print("What's your command, sir?")
    text = takeCommand()   # Get user's command through voice input

    # This is for opening websites
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
             ["google", "https://www.google.com"], ["github", "https://github.com/"]]

    # Opening the site in the list of lists
    for site in sites:
        if f"Open {site[0]}".lower() in text.lower():
            speak(f"Opening {site[0]}, sir...")  # Speak confirmation
            webbrowser.open(site[1])             # Open the website in the browser

    # For getting the time
    if "What's the time".lower() in text:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")  # Get current time
        speak(f"Sir, the time is {current_time}")                     # Speak the time

    # For opening applications
    apps = [["vs code", "Visual Studio Code"], ["whatsapp", "Whatsapp"], ["Dev C", "Dev-C++"],
            ["pycharm", "PyCharm Community Edition 2023.1.2"]]

    # Opening the app in the list of lists
    for app in apps:
        if f"Open {app[0]}".lower() in text.lower():
            speak(f"Opening {app[0]}, sir...")  # Speak confirmation
            open(app[1])                        # Open the application

    # For asking questions and retrieving answers from Google
    if "I have some questions".lower() in text.lower():
        speak("Alright! What's your question, sir...")  # Prompt the user to ask a question
        question = takeCommand()                        # Get the question through voice input
        speak(f"Your question is: {question}")          # Confirm the question
        print("Searching for the answer! Please Wait...")
        speak(f"Searching for the answer! Please Wait...")

        try:
            # Fetching Google search results
            url = f"https://www.google.com/search?q={question}"  # Construct the Google search URL
            headers = {'User-Agent': 'Mozilla/5.0'}              # Set user-agent header
            response = requests.get(url, headers=headers)        # Send HTTP request
            soup = BeautifulSoup(response.text, 'html.parser')   # Parse the HTML response
            results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')  # Find relevant elements in the HTML

            # Extracting and speaking the answer
            found_answer = False
            for result in results:
                answer = result.get_text()                     # Get the text content of the result
                # Checking if the answer is relevant
                if len(answer.split()) > 10:                   # Ensure the answer is not too short
                    print(answer)                             # Print the answer
                    speak(answer)                             # Speak the answer
                    found_answer = True
                    break

            if not found_answer:
                print("Sorry, I couldn't find an answer.")
                speak("Sorry, I couldn't find an answer.")

        except Exception as e:
            print(f"An error occurred: {e}")
            speak("Sorry, an error occurred while fetching information.")
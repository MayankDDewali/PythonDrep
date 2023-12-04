# pip install pyttsx3
import pyttsx3

# pip install wikipedia
import wikipedia

voice = pyttsx3.init()
Qs = input("Searching wikipedia/google: ")
sentence = int(input("Enter then number of sentence you want: "))
result = wikipedia.summary(Qs, sentence)

print(result)
voice.say(result)
voice.runAndWait()
# Importing required library for tkinter
import tkinter as tk

# Importing required libraries for AI Project
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


def left_button_click():
    print("Left button clicked")

def right_button_click():
    print("Right button clicked")

def middle_button_click():
    print("Middle button clicked")

# Create the main application window
root = tk.Tk()
root.title("Trial AI Program")
root.geometry("900x500")

# Calculate dimensions for the divs
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

div_width = window_width * 0.25
div_height = window_height * 0.2

# Create top div
top_div = tk.Frame(root, width=window_width, height=div_height, bg="lightgreen", highlightthickness=2, highlightbackground="black")
top_div.pack(side="top", fill="both", expand=True)

# Add label to top div
label_top = tk.Label(top_div, text="This is a trial AI Project")
label_top.pack()

# Create left div
left_div = tk.Frame(root, width=div_width, height=div_height, bg="lightblue", highlightthickness=2, highlightbackground="black")
left_div.pack(side="left", fill="both", expand=True)

# Add label to left div
label_left = tk.Label(left_div, text="Open Sites")
label_left.pack(pady=20)

# Create button in left div
left_button = tk.Button(left_div, text="Left Button", command=left_button_click)
left_button.pack(pady=180)

# Create middle div
middle_div = tk.Frame(root, bg="lightgrey", highlightthickness=2, highlightbackground="black")
middle_div.pack(side="left", fill="both", expand=True)

# Create button in middle div
middle_button = tk.Button(middle_div, text="Middle Button", command=middle_button_click)
middle_button.pack(pady=(window_height * 0.4, window_height * 0.4))

# Create right div
right_div = tk.Frame(root, width=div_width, height=div_height, bg="lightblue", highlightthickness=2, highlightbackground="black")
right_div.pack(side="left", fill="both", expand=True)

# Add label to right div
label_right = tk.Label(right_div, text="Open Applications")
label_right.pack(pady=20)

# Create button in right div
right_button = tk.Button(right_div, text="Right Button", command=right_button_click)
right_button.pack(pady=180)


# Run the Tkinter event loop
root.mainloop()
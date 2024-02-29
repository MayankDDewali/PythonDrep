from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import filedialog
import platform

import psutil

# Brightness Library
import screen_brightness_control as pct

# Audio Library
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Weather Library
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# Clock Library
from time import strftime

# Calendar Library
from tkcalendar import *

# Open Google Library
# import Pyautogui

# For AI
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import requests
from AppOpener import open
from bs4 import BeautifulSoup

# Starting the tkinter code
root = Tk()
root.title("TrialProject")
root.geometry("850x500+320+170")
root.resizable(False,False)
root.configure(bg='#292e2e')

# Image Icon
image_icon = PhotoImage(file="TkinterProjects/Images/DarkDD13logo2.png")
root.iconphoto(False,image_icon)

Body = Frame(root, width=900, height=600, bg="#d6d6d6")
Body.pack(padx=20, pady=20)

LHS = Frame(Body,width=310, height=435, bg="#f4f5f5", highlightbackground="#adacb1", highlightthickness=1)
LHS.place(x=10, y=10)



############################################################## LHS Part ##############################################################
# Laptop Image
photo=PhotoImage(file="TkinterProjects/Images/Laptop.png")
photo = photo.subsample(2, 2)
myimage = Label(LHS,image=photo,background="#f4f5f5")
myimage.place(x=23,y=20)

# For getting the name and version of my device
my_system = platform.uname()

l1 = Label(LHS, text=my_system.node, font=("Acumin Variable Concept", 14, "bold"))
l1.place(x=20, y=205)

l2 = Label(LHS, text=f"Version: {my_system.version}", font=("Acumin Variable Concept", 8, "bold"))
l2.place(x=20, y=230)

l3 = Label(LHS, text=f"System: {my_system.system}", font=("Acumin Variable Concept", 15, "bold"))
l3.place(x=20, y=250)

l4 = Label(LHS, text=f"Machine: {my_system.machine}", font=("Acumin Variable Concept", 15, "bold"))
l4.place(x=20, y=285)

l5 = Label(LHS, text=f"Total RAM installed: {round(psutil.virtual_memory().total/1000000000,2)} GB", font=("Acumin Variable Concept", 8, "bold"))
l5.place(x=20, y=315)

l6 = Label(LHS, text=f"Processor: {my_system.processor}", font=("Acumin Variable Concept", 6,'bold'))
l6.place(x=20, y=340)

############################################################## RHS1 part ##############################################################
RHS1 = Frame(Body,width=470, height=230, bg="#f4f5f5", highlightbackground="#adacb1", highlightthickness=1)
RHS1.place(x=330, y=10)

system = Label(RHS1, text="System", font=("Acumin Variable Concept", 15), bg="#f4f5f5")
system.place(x=10, y=10)


def convertTime(seconds):
    minutes,seconds=divmod(seconds,60)
    hours,minutes=divmod(minutes,60)
    return "%d:%02d:%02d"%(hours,minutes,seconds)

def none():
    global battery_png
    global battery_label
    battery=psutil.sensors_battery()
    percent=battery.percent
    time=convertTime(battery.secsleft)
    
    lbl.config(text=f"{percent}%")
    lbl_plug.config(text=f"Plug in:{str(battery.power_plugged)}")
    lbl_time.config(text=f"{time} remaining time")

    battery_label=Label(RHS1, background="#f4f5f5")
    battery_label.place(x=15, y=50)

    lbl.after(1000,none)
    
    if battery.power_plugged==True:
        battery_png=PhotoImage(file="TkinterProjects/Images/Charging.png")
        battery_label.config(image=battery_png)
        # battery_png = battery_png.subsample(1, 1)
    else:
        battery_png=PhotoImage(file="TkinterProjects/Images/Battery.png")
        battery_label.config(image=battery_png)
        # battery_png = battery_png.subsample(1, 1)



lbl = Label(RHS1, font=("Acumin Variable Concept", 40), bg="#f4f5f5")
lbl.place(x=200, y=40)

lbl_plug = Label(RHS1, font=("Acumin Variable Concept", 10), bg="#f4f5f5")
lbl_plug.place(x=20, y=100)

lbl_time = Label(RHS1, font=("Acumin Variable Concept", 15), bg="#f4f5f5")
lbl_time.place(x=200, y=100)

none()


############################################################### Speaker ###############################################################
lbl_speaker = Label(RHS1, text="Speaker:", font=('arial',10,'bold'),bg="#f4f5f5")
lbl_speaker.place(x=10,y=150)
volume_value = tk.DoubleVar()

def get_current_volume_value():
    return '{: .2f}'.format(volume_value.get())

def volume_changed(event):
    device = AudioUtilities.GetSpeakers()
    interface = device.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(-float(get_current_volume_value()), None)
    
style = ttk.Style()
style.configure("TScale", background='#f4f5f5')
    
volume = ttk.Scale(RHS1, from_=60, to=0, orient='horizontal',command=volume_changed,variable=volume_value)
volume.place(x=90, y=150)
volume.set(20)


############################################################## Brightness ##############################################################
lbl_brightness = Label(RHS1,text='Brightness',font=('arial',10,'bold'),bg="#f4f5f5")
lbl_brightness.place(x=10,y=190)

current_value=tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def brightness_changed(event):
    pct.set_brightness(get_current_value())
    
brightness = ttk.Scale(RHS1, from_=0, to=100, orient='horizontal', command=brightness_changed, variable=current_value)
brightness.place(x=90,y=190)

############################################################## RHS2 part ##############################################################
RHS2 = Frame(Body,width=470, height=190, bg="#f4f5f5", highlightbackground="#adacb1", highlightthickness=1)
RHS2.place(x=330, y=255)

apps=Label(RHS2,text='Apps',font=('Acumin Variable Concept',15),bg="#f4f5f5")
apps.place(x=10,y=10)

################### Making Apps ###################

def weather():
    app1=Toplevel()
    app1.geometry('850x500+320+170')
    app1.title('Weather')
    app1.configure(bg='#f4f5f5')
    app1.resizable(False,False)
    
    # For making weather icon
    image_icon=PhotoImage(file="TkinterProjects/Images/Weather.png")
    app1.iconphoto(False,image_icon)
    
    def getWeather():
        try:
            city=textfield.get()
            
            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.geocode(city)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat = location.latitude)
            
            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            name.config(text="CURRENT WEATHER")
            
            api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"
            
            json_data = requests.get(api).json()
            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp']-273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']
            
            t.config(text=(temp,"°"))
            c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
            
            w.config(text=wind)
            h.config(text=humidity)
            d.config(text=description)
            p.config(text=pressure)
            
            
            
        except Exception as e:
            messagebox.showerror("Weatehr App", "Invalid Entry!")
            
    
    # Search Box
    # Search_image=PhotoImage(file="TkinterProjects/Images/search.png")
    # myimage=Label(app1,image=Search_image,bg="#f4f5f5")
    # myimage.place(x=20,y=20)
    
    textfield=tk.Entry(app1,justify='center', width=17, font=('poppins',25,'bold'),bg="#404040",border=0,fg="white")
    textfield.place(x=50,y=40)
    textfield.focus()
    
    Search_icon = PhotoImage(file="TkinterProjects/Images/search_icon.png")
    myimage_icon = Button(app1,image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
    myimage_icon.place(x=340,y=40)
    
    # Logo
    logo_image = PhotoImage(file="TkinterProjects/Images/WeatherLogo.png")
    logo = Label(app1,image=logo_image, bg="#f4f5f5")
    logo.place(x=150, y=100)
    
    # Bottom Box
    Frame_image = PhotoImage(file="TkinterProjects/Images/BlueBox.png")
    frame_myimage = Label(app1,image=Frame_image, bg="#f4f5f5")
    frame_myimage.pack(padx=5, pady=5, side=BOTTOM)
    
    # Time
    name = Label(app1,font=('arial', 15, 'bold'), bg="#f4f5f5")
    name.place(x=30, y=100)
    clock=Label(app1,font=('Helvetica',20),bg="#f4f5f5")
    clock.place(x=30, y=130)
    
    # Label
    labell1=Label(app1, text="WIND", font=("Helvatica", 15, "bold"), fg="white", bg="#0b98dc")
    labell1.place(x=110, y=420)
    
    labell2=Label(app1, text="HUMIDITY", font=("Helvatica", 15, "bold"), fg="white", bg="#0b98dc")
    labell2.place(x=240, y=420)
    
    labell3=Label(app1, text="DESCRIPTION", font=("Helvatica", 15, "bold"), fg="white", bg="#0b98dc")
    labell3.place(x=420, y=420)
    
    labell4=Label(app1, text="PRESSURE", font=("Helvatica", 15, "bold"), fg="white", bg="#0b98dc")
    labell4.place(x=640, y=420)
    
    
    t = Label(app1, font=('arial', 70, 'bold'), fg="#ee666d", bg="#f4f5f5")
    t.place(x=400, y=150)
    
    c = Label(app1, font=('arial', 15, 'bold'), bg="#f4f5f5")
    c.place(x=400, y=250)


    w=Label(app1, text="...", font=('arial', 20, 'bold'), bg="#0b98dc")
    w.place(x=115, y=450)
    h=Label(app1, text="...", font=('arial', 20, 'bold'), bg="#0b98dc")
    h.place(x=280, y=450)
    d=Label(app1, text="...", font=('arial', 20, 'bold'), bg="#0b98dc")
    d.place(x=410, y=450)
    p=Label(app1, text="...", font=('arial', 20, 'bold'), bg="#0b98dc")
    p.place(x=670, y=450)
    
    app1.mainloop()
    
    
app1_image=PhotoImage(file="TkinterProjects/Images/Weather.png")
app1=Button(RHS2,image=app1_image,bd=0,command=weather)
app1.place(x=15,y=35)

labell5=Label(app1, text="Weather", font=("Helvatica", 10, "bold"), fg="white", bg="black")
labell5.place(x=0, y=40)


##################################################### Clock #####################################################
def clock():
    app2 = Toplevel()
    app2.geometry("850x110+320+30")
    app2.title('Clock')
    app2.configure(bg="#292e2e")
    app2.resizable(False,False)
    
    image_icon=PhotoImage(file="TkinterProjects/Images/Clock.png")
    app2.iconphoto(False,image_icon)
    
    def clock():
        text=strftime('%H:%M:%S %p')
        lbl.config(text=text)
        lbl.after(1000,clock)
    
    lbl = Label(app2,font=('digital-7',50,'bold'),width=20,bg="#f4f5f5",fg="#292e2e")
    lbl.pack(anchor="center",pady=20)
    
    clock()
    
    
    app2.mainloop()
    
    
    
app2_image=PhotoImage(file="TkinterProjects/Images/Clock.png")
app2=Button(RHS2,image=app2_image,bd=0, command=clock)
app2.place(x=100,y=35)

labell6=Label(app2, text="Clock", font=("Helvatica", 10, "bold"), fg="white", bg="black")
labell6.place(x=15, y=40)

################################################# For opening the applicatiuons #################################################

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

def open_app():
    # Initialize the text-to-speech engine
    voice_engine = pyttsx3.init()
    
    # Speak and prompt the user to specify which app they want to open
    voice_engine.say("Which application would you like to open?")
    voice_engine.runAndWait()

    text = takeCommand()   # Get user's command through voice input
    
    # Here, you would call your existing function that handles opening applications based on user input
    # For now, let's print a message to simulate opening the app
    print("Opening application based on user input...")
    
    
    # For opening applications
    apps = [["vs code", "Visual Studio Code"], ["whatsapp", "Whatsapp"], ["Dev C", "Dev-C++"],
            ["pycharm", "PyCharm Community Edition 2023.1.2"]]

    # Opening the app in the list of lists
    for app in apps:
        if f"open {app[0]}".lower() in text.lower():
            voice_engine.say(f"Opening {app[0]}, sir...")  # Speak confirmation
            voice_engine.runAndWait()
            open(app[1])                        # Open the application
            return  # Exit the function after opening the app

    # If the user's command doesn't match any known app, inform them
    voice_engine.say("Sorry, I couldn't understand which app you want to open.")
    voice_engine.runAndWait()


app3_image=PhotoImage(file="TkinterProjects/Images/btn4.png")
app3=Button(RHS2,image=app3_image,bd=0, command=open_app)
app3.place(x=185,y=35)

labell7=Label(app3, text="Apps", font=("Helvatica", 10, "bold"), fg="white", bg="black")
labell7.place(x=13, y=40)

################################################# For opening the sites #################################################

def open_sites():
    # Initialize the text-to-speech engine
    voice_engine = pyttsx3.init()
    
    # Speak and prompt the user to specify which site they want to open
    voice_engine.say("Which site would you like to open?")
    voice_engine.runAndWait()

    text = takeCommand()   # Get user's command through voice input
    
    # Here, you would call your existing function that handles opening websites based on user input
    # For now, let's print a message to simulate opening the site
    print("Opening Sites based on user input...")
    
    
    # List of websites to open
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
             ["google", "https://www.google.com"], ["github", "https://github.com/"]]

    # Opening the site in the list of lists
    for site in sites:
        if f"open {site[0]}".lower() in text.lower():
            voice_engine.say(f"Opening {site[0]}, sir...")  # Speak confirmation
            voice_engine.runAndWait()
            webbrowser.open(site[1])             # Open the website in the browser
            return  # Exit the function after opening the site

    # If the user's command doesn't match any known site, inform them
    voice_engine.say("Sorry, I couldn't understand which site you want to open.")
    voice_engine.runAndWait()



app4_image=PhotoImage(file="TkinterProjects/Images/btn2.png")
app4=Button(RHS2,image=app4_image,bd=0, command=open_sites)
app4.place(x=270,y=35)

labell8=Label(app4, text="Sites", font=("Helvatica", 10, "bold"), fg="white", bg="black")
labell8.place(x=13, y=40)

######################################################## For Asking Questions ########################################################

def AskQues():
    # Initialize the text-to-speech engine
    voice_engine = pyttsx3.init()
    
    # Speak and prompt the user to ask a question
    voice_engine.say("What's your question, sir?")
    voice_engine.runAndWait()

    question = takeCommand()                        # Get the question through voice input
    
    voice_engine.say(f"Your question is: {question}")          # Confirm the question
    voice_engine.runAndWait()
    
    print("Searching for the answer! Please wait...")
    
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
                voice_engine.say(answer)                   # Speak the answer
                voice_engine.runAndWait()
                found_answer = True
                break

        if not found_answer:
            print("Sorry, I couldn't find an answer.")
            voice_engine.say("Sorry, I couldn't find an answer.")
            voice_engine.runAndWait()

    except Exception as e:
        print(f"An error occurred: {e}")
        voice_engine.say("Sorry, an error occurred while fetching information.")
        voice_engine.runAndWait()


app5_image=PhotoImage(file="TkinterProjects/Images/btn3.png")
app5=Button(RHS2,image=app5_image,bd=0, command=AskQues)
app5.place(x=355,y=35)

labell9=Label(app5, text="Ask", font=("Helvatica", 10, "bold"), fg="white", bg="black")
labell9.place(x=17, y=40)

############################################################# For Talking #############################################################

def Talkk():
    try:
        while True:  # Continuously listen for commands until a valid one is received
            # Initialize the text-to-speech engine
            voice_engine = pyttsx3.init()

            # Get the command through voice input
            print("Listening...")
            command = takeCommand().lower()

            # Check if the user said "introduce yourself"
            if "introduce yourself".lower() in command:
                # Speak introduction
                voice_engine.say("Alright Mister Mayank")
                voice_engine.runAndWait()
                voice_engine.say("Hello everyone, I am Project, an AI created by Mr. Mayank. Powered by a blend of libraries including tkinter, psutil, screen_brightness_control, and more, I am equipped with a variety of funct+ions. Need to know the weather in different cities? I've got you covered. Want to check the time? I have an inbuilt clock. Curious about your system's specs? I can provide information on your system's name, version, processor, RAM, and more. Plus, I have the ability to adjust system volume and brightness. With the power of speech, I can engage in conversation, answer questions using Google, and even open websites and apps for you. Consider me a trial project; Mr. Mayank plans to enhance my capabilities in the future. Thank you for interacting with me!")
                voice_engine.runAndWait()
                break  # Exit the loop after a valid command is processed
            elif "libraries I have used for creating you".lower() in command:
                # Speak about libraries used
                voice_engine.say('''Throughout my creation process, Mr. Mayank carefully selected a variety of libraries to empower me with diverse functionalities. Here's a glimpse into the toolkit he employed:
                                    GUI Libraries: tkinter, ttk, filedialog - Crafting the user interface.
                                    System Information Libraries: platform, psutil - Gathering system insights.
                                    Brightness Control Library: screen_brightness_control - Adjusting screen brightness.
                                    Audio Control Libraries: ctypes, comtypes, pycaw - Managing audio settings.
                                    Weather Libraries: geopy, timezonefinder, datetime, requests, pytz - Providing weather updates.
                                    Clock Library: time - Displaying the current time.
                                    Calendar Library: tkcalendar - Assisting with date-related tasks.
                                    Speech Recognition and Text-to-Speech Libraries: speech_recognition, pyttsx3 - Enabling voice interactions.
                                    Web Interaction Libraries: webbrowser, requests, bs4 - Navigating the web and fetching information.
                                    Custom Library: AppOpener - Handling application operations.
                                    Each library contributes uniquely to my capabilities, allowing me to serve you better.''')
                voice_engine.runAndWait()
                break  # Exit the loop after a valid command is processed
            else:
                # Say "Sorry, an error occurred in hearing the command."
                voice_engine.say("Sorry, an error occurred in hearing the command.")
                voice_engine.runAndWait()
                continue  # Continue listening for commands in the loop

    except Exception as e:
        print(f"An error occurred: {e}")
        # Inform the user about the error
        voice_engine.say("Sorry, an error occurred while processing your request.")
        voice_engine.runAndWait()
    

app6_image=PhotoImage(file="TkinterProjects/Images/lastbtn.png")
app6=Button(RHS2,image=app6_image,bd=0, command=Talkk)
app6.place(x=15,y=120)

labell10=Label(app6, text="Talk", font=("Helvatica", 10, "bold"), fg="white", bg="black")
labell10.place(x=15, y=40)

root.mainloop()
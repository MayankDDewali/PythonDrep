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

import subprocess
import webbrowser as wb
import random


# Starting the tkinter code
root = Tk()
root.title("TrialProject")
root.geometry("850x500+320+170")
root.resizable(False,False)
root.configure(bg='#292e2e')

# Image Icon
image_icon = PhotoImage(file="TkinterProjects\Images\DarkDD13logo2.png")
root.iconphoto(False,image_icon)

Body = Frame(root, width=900, height=600, bg="#d6d6d6")
Body.pack(padx=20, pady=20)

LHS = Frame(Body,width=310, height=435, bg="#f4f5f5", highlightbackground="#adacb1", highlightthickness=1)
LHS.place(x=10, y=10)



############################################################## LHS Part ##############################################################
# Laptop Image
photo=PhotoImage(file="TkinterProjects\Images\Laptop.png")
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
lbl_speaker = Label(RHS1, text="Speacker:", font=('arial',10,'bold'),bg="#f4f5f5")
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


############################################################### Speaker ###############################################################
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
    app1.geometry('850x500+300+170')
    app1.title('Weather')
    app1.configure(bg='#f4f5f5')
    app1.resizable(False,False)
    app1.mainloop()
    
    # For making weather icon
    image_icon=PhotoImage(file="TkinterProjects")
    
app1_image=PhotoImage(file="TkinterProjects/Images/Weather.png")
app1=Button(RHS2,image=app1_image,bd=0,command=weather)
app1.place(x=15,y=45)

app2_image=PhotoImage(file="TkinterProjects/Images/Clock.png")
app2=Button(RHS2,image=app2_image,bd=0)
app2.place(x=100,y=45)

app3_image=PhotoImage(file="TkinterProjects/Images/Weather.png")
app3=Button(RHS2,image=app3_image,bd=0)
app3.place(x=185,y=45)

app4_image=PhotoImage(file="TkinterProjects/Images/Weather.png")
app4=Button(RHS2,image=app4_image,bd=0)
app4.place(x=270,y=45)

app5_image=PhotoImage(file="TkinterProjects/Images/Weather.png")
app5=Button(RHS2,image=app5_image,bd=0)
app5.place(x=355,y=45)

app6_image=PhotoImage(file="TkinterProjects/Images/Weather.png")
app6=Button(RHS2,image=app6_image,bd=0)
app6.place(x=15,y=110)

app7_image=PhotoImage(file="TkinterProjects/Images/Weather.png")
app7=Button(RHS2,image=app7_image,bd=0)
app7.place(x=100,y=110)

app8_image=PhotoImage(file="TkinterProjects/Images/Weather.png")
app8=Button(RHS2,image=app8_image,bd=0)
app8.place(x=185,y=110)

app9_image=PhotoImage(file="TkinterProjects/Images/Weather.png")
app9=Button(RHS2,image=app9_image,bd=0)
app9.place(x=270,y=110)

app10_image=PhotoImage(file="TkinterProjects/Images/Weather.png")
app10=Button(RHS2,image=app10_image,bd=0)
app10.place(x=355,y=110)

root.mainloop()
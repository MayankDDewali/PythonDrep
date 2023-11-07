import tkinter                    #other method of importing py-library
from tkinter import *
from PIL import Image, ImageTk      #for other photos(not png)
root=Tk()                           #for making the object
root.title("Hello world")           #for adding title
root.geometry("900x500")            #width*height
root.minsize(300,100)               #for minimum size
# root.maxsize(1000,1000)           #for maximum size
text=Label(text="This is tkinter class",background="red")    #for text
text.pack()             #without this text will not work(basically it is a syntax)
# text.grid()             #another mehod for pack

# photo=PhotoImage(file="hello.png")            #for png image
# label=Label(image=photo)
# label.pack()

#.pack() is important

image=Image.open("hello2.jpg")         #for jpg image
photo=ImageTk.PhotoImage(image)
label=Label(image=photo)
label.pack()
# label=Label(text="this is my text this is my text this is my text",bg="red")
root.mainloop()                         #for holding the screen
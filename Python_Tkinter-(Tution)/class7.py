from tkinter import *
import tkinter.messagebox as msg
root=Tk()
root.title("Hello World")
root.geometry("900x500")

def func():
    print("Hello I am Mayank")
def help():
    msg.showinfo("Help","Yes sure we'll definately help you")
    v=msg.askquestion("Question","Do you like our application")
    print(v)
    if v=="yes":
        msg.showinfo("","Rate us on playstore")
    else:
        msg.showinfo("","Our team will contact you")

filemenu=Menu(root)                                             #for making menu

#for submenu
m1=Menu(filemenu,tearoff=0)
m1.add_command(label="file",command=func)
m1.add_command(label="Save",command=func)
m1.add_command(label="Save as",command=func)
m1.add_command(label="Help me",command=help)

#for adding seprator
m1.add_separator()

m1.add_command(label="Exit",command=quit)
m1.add_command(label="Print",command=func)

m2=Menu(filemenu,tearoff=0)
m2.add_command(label="Edit",command=func)
m2.add_command(label="Edit from VS Code")
m2.add_command(label="Edit from pycharm",command=func)
m2.add_command(label="Exit",command=quit)

filemenu.add_command(label="file",command=func)                 #for adding file in menu
filemenu.add_command(label="Exit",command=quit)                 #for adding exit in menu
root.config(menu=filemenu)

filemenu.add_cascade(label="File",menu=m1)
filemenu.add_cascade(label="Edit",menu=m2)

root.mainloop()
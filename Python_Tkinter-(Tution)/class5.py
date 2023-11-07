from tkinter import *                   #for importing tkinter
root=Tk()                               #making a object
root.title("Form")

def getvalue():
    f=open("class4.txt","a")
    print(uservalue.get())
    print(passvalue.get())
    print(rolvalue.get())
    f.write(f'{uservalue.get(),passvalue.get(),rolvalue.get()}')

f1=Frame(root,bg="gray",borderwidth=5,relief=GROOVE)                #for making divison(div)
f1.grid(relx=0.5,rely=0.5,anchor=CENTER)             #for sliding the frame(div) to left

root.geometry("900x500")                #giving the screen proper geometry

user=Label(f1,text="username")        #for asking the username
user.grid(row=0)                        #another method for using pack()
password=Label(f1,text="password")    #for asking the password
password.grid(row=1)
roll=Label(f1,text="roll")            #for asking roll number
roll.grid(row=2)

uservalue=StringVar()
passvalue=StringVar()
rolvalue=StringVar()

userentery=Entry(f1,textvariable=uservalue)
passentery=Entry(f1,textvariable=passvalue)
rolentery=Entry(f1,textvariable=rolvalue)

userentery.grid(row=0,column=1)
passentery.grid(row=1,column=1)
rolentery.grid(row=2,column=1)

Button(f1,text="Submit",command=getvalue).grid()

root.mainloop()                          #for holding the screen
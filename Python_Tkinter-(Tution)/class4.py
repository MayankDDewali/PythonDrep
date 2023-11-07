from tkinter import *
root=Tk()
def getvalue():
    f=open("class4.txt","w")
    # f.write(uservalue.get()+"\n")
    # f.write(passvalue.get())
    print(uservalue.get())
    print(passvalue.get())
    f.write(f'{uservalue.get(),passvalue.get()}')

root.geometry("800x600")
user=Label(root,text="username")
user.grid(row=0)             #another method for using pack()
password=Label(root,text="password")
password.grid(row=1)

uservalue=StringVar()
passvalue=StringVar()

userentery=Entry(root,textvariable=uservalue)
passentery=Entry(root,textvariable=passvalue)

userentery.grid(row=0,column=1)
passentery.grid(row=1,column=1)

Button(text="Submit",command=getvalue).grid()

root.mainloop()
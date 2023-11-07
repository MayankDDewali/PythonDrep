from tkinter import *
import mysql.connector as msql
import tkinter.messagebox as msg

con=msql.connect(host="localhost",user="root",password="mayankdd13")
cur=con.cursor()
try:
    cur.execute("use bank")
except:
    cur.execute("create database bank")
    cur.execute("use bank")


logi=Tk()
logi.geometry("600x400")
logi.title("login page")

def login():
    query="select * from bankinfo where name=%s and password=%s"
    cur.execute(query,(e1.get(),e6.get()))
    data=cur.fetchone()
    if data==None:
        msg.showinfo("","login unsuccessful")
    else:
        msg.showinfo("","login successful")


l1=Label(logi,text="Name")
l6=Label(logi,text="Password")

l1.grid(row=1,column=1)
l6.grid(row=2,column=1)

e1 = StringVar()
e6 = StringVar()

e1=Entry(logi,textvariable=e1)
e6=Entry(logi,textvariable=e6)

e1.grid(row=1,column=2)
e6.grid(row=2,column=2)

def sig():
    logi.destroy()
    import project

def forget():
    logi.destroy()
    import password

b1=Button(logi,text="login",command=login)
b1.grid(row=3,column=1)
b2=Button(logi,text="Sign up",command=sig)
b2.grid(row=3,column=2)
b3=Button(logi,text="Forget password",command=forget)
b3.grid(row=3,column=3)


logi.mainloop()
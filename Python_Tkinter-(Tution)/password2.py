from tkinter import *
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
    query="select * from bankinfo where SecretQs=%s"
    cur.execute(query,(e1.get()))
def new():
    query = "UPDATE bankinfo SET password =%s WHERE SecretQs = %s;"
    cur.execute(query,(e1.get(),e2.get()))
    data = cur.fetchone()

def fors():
    query="select * from bankinfo where SecretQs=%s"
    cur.execute(query,(e2.get(),e1.get()))
    data=cur.fetchone()
    if data==None:
        msg.showinfo("","Changes Successful")
    else:
        msg.showinfo("","Changes Unsuccessful")

l1=Label(logi,text="SecretQs")

l1.grid(row=1,column=1)

e1 = StringVar()

e1=Entry(logi,textvariable=e1)

e1.grid(row=1,column=2)


b1=Button(logi,text="Submit",command=fors)
b1.grid(row=7,column=2)

l1=Label(logi,text="SecretQs")

l1.grid(row=2,column=1)

e1 = StringVar()

e1=Entry(logi,textvariable=e1)

e1.grid(row=2,column=2)

l2=Label(logi,text="New password")

l2.grid(row=1,column=1)

e2 = StringVar()

e2=Entry(logi,textvariable=e2)

e2.grid(row=1,column=2)

b2=Button(logi,text="Submit",command=new)
b2.grid(row=7,column=2)

logi.mainloop()
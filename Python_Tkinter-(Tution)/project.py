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


root=Tk()
root.geometry("600x400")
root.title("Create account page")


l1=Label(root,text="Name")
l2=Label(root,text="Age")
l3=Label(root,text="Gender")
l4=Label(root,text="EMail")
l5=Label(root,text="Mobile_no")
l6=Label(root,text="password")
l7=Label(root,text="SecretQs")


name = StringVar()
age = StringVar()
gender = StringVar()
email = StringVar()
mobileno = StringVar()
password = StringVar()
secret=StringVar()


l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
l3.grid(row=3,column=1)
l4.grid(row=4,column=1)
l5.grid(row=5,column=1)
l6.grid(row=6,column=1)
l7.grid(row=7,column=1)


e1=Entry(root,textvariable=name)
e2=Entry(root,textvariable=age)
e3=Entry(root,textvariable=gender)
e4=Entry(root,textvariable=email)
e5=Entry(root,textvariable=mobileno)
e6=Entry(root,textvariable=password)
e7=Entry(root,textvariable=secret)


e1.grid(row=1,column=2)
e2.grid(row=2,column=2)
e3.grid(row=3,column=2)
e4.grid(row=4,column=2)
e5.grid(row=5,column=2)
e6.grid(row=6,column=2)
e7.grid(row=7,column=2)


def registration():
    try:
        cur.execute(f"INSERT INTO bankinfo (Name, Age, Gender, EMail, Mobile_no, password, Secret_Qs) VALUES ('{e1.get()}', '{e2.get()}', '{e3.get()}', '{e4.get()}', '{e5.get()}', '{e6.get()}', '{e7.get()}')")
        con.commit()
    except:
        cur.execute("create table bankinfo(Name varchar(20),Age varchar(20),Gender varchar(10),EMail varchar(30),Mobile_no varchar(20),password varchar(20),Secret_Qs(30)")
        cur.execute(f"INSERT INTO bankinfo (Name, Age, Gender, EMail, Mobile_no, password, Secret_Qs) VALUES ('{e1.get()}', '{e2.get()}', '{e3.get()}', '{e4.get()}', '{e5.get()}, '{e6.get()}', '{e7.get()}')")
        con.commit()

def login():
    root.destroy()
    import loginn


b=Button(root,text="Login",command=login)
b.grid(row=8,column=1)


b1=Button(root,text="Submit",command=registration)
b1.grid(row=8,column=2)


root.mainloop()
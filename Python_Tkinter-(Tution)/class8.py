from tkinter import *
import mysql.connector as msql
con=msql.connect(host="localhost",user="root",password="mayankdd13")
cur=con.cursor()
try:
    cur.execute("use registration")
except:
    cur.execute("create database registration")
    cur.execute("use registration")


root=Tk()
root.geometry("600x400")
root.title("Registration form")
l1=Label(root,text="Name")
l2=Label(root,text="Age")
l3=Label(root,text="Gender")
l4=Label(root,text="EMail")
l5=Label(root,text="Mobile_no")
l6=Label(root,text="password")

name = StringVar()
age = StringVar()
gender = StringVar()
email = StringVar()
mobileno = StringVar()
password = StringVar()

l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
l3.grid(row=3,column=1)
l4.grid(row=4,column=1)
l5.grid(row=5,column=1)
l6.grid(row=6,column=1)


e1=Entry(root,textvariable=name)
e2=Entry(root,textvariable=age)
e3=Entry(root,textvariable=gender)
e4=Entry(root,textvariable=email)
e5=Entry(root,textvariable=mobileno)
e6=Entry(root,textvariable=password)

e1.grid(row=1,column=2)
e2.grid(row=2,column=2)
e3.grid(row=3,column=2)
e4.grid(row=4,column=2)
e5.grid(row=5,column=2)
e6.grid(row=6,column=2)

def registration():
    try:
        cur.execute(f"INSERT INTO pysql (Name, Age, Gender, EMail, Mobile_no, password) VALUES ('{name.get()}', '{age.get()}', '{gender.get()}', '{email.get()}', '{mobileno.get()}', '{password.get()}')")
        con.commit()
    except:
        cur.execute("create table pysql(Name varchar(20),Age varchar(20),Gender varchar(10),EMail varchar(30),Mobile_no varchar(20),password varchar(20))")
        cur.execute(f"INSERT INTO pysql (Name, Age, Gender, EMail, Mobile_no, password) VALUES ('{name.get()}', '{age.get()}', '{gender.get()}', '{email.get()}', '{mobileno.get()}, '{password.get()}'')")
        con.commit()

b=Button(root,text="Submit",command=registration)
b.grid(row=7,column=1)

root.mainloop()
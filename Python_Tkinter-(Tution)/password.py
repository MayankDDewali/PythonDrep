from tkinter import *
import mysql.connector as msql
import tkinter.messagebox as msg

con = msql.connect(host="localhost", user="root", password="mayankdd13", database="bank")
cur = con.cursor()

logi = Tk()
logi.geometry("600x400")
logi.title("login page")

def fors():
    query = "SELECT * FROM bankinfo WHERE Secret_Qs = %s"
    cur.execute(query, (e1.get(),))
    data = cur.fetchone()
    if data is not None:
        new_password = e2.get()
        try:
            cur.execute("UPDATE bankinfo SET password = %s WHERE Secret_Qs = %s", (new_password, e1.get()))
            con.commit()
        except msql.Error as err:
            msg.showerror("Error", f"Failed to update password: {err}")
        else:
            msg.showinfo("", "Password updated successfully")
    else:
        msg.showinfo("", "Incorrect answer!...")

l1 = Label(logi, text="SecretQs")
l1.grid(row=1, column=1)

e1 = StringVar()
e1_entry = Entry(logi, textvariable=e1)
e1_entry.grid(row=1, column=2)

l2 = Label(logi, text="New password")
l2.grid(row=2, column=1)

e2 = StringVar()
e2_entry = Entry(logi, textvariable=e2)
e2_entry.grid(row=2, column=2)

b1 = Button(logi, text="Submit", command=fors)
b1.grid(row=3, column=1)

logi.mainloop()
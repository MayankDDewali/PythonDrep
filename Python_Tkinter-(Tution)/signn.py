from tkinter import *

signn=Tk()
signn.geometry("600x400")
def sign():
    signn.destroy()
    import loginn

l1=Label(signn,text="signup page").grid()
b1=Button(signn,text="sign_up",command=sign)
b1.grid(row=2,column=1)


tree=ttk.Treeview()
tree["columns"]=["email","name","phone"]


signn.mainloop()
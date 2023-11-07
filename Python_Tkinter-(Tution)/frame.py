from tkinter import *
root=Tk()
root.geometry("800x600")

def func():
    print("Hello world")

def func1():
    f=open("text.txt","w")
    f.write("Hello I am mayank")

f1=Frame(root,bg="gray",borderwidth=5,relief=GROOVE)                #for making divison(div)
f1.pack(side=LEFT,fill=Y)               #for sliding the frame(div) to left

f2=Frame(root,bg="gray",borderwidth=5,relief=GROOVE)                #for making divison(div)
f2.pack(side=TOP, fill=X)

l=Label(f1,text="hello world")              #f1,  for adding something to the frame2
l.pack(pady=150)

l=Label(f2,text="div2")                     #f2,  for adding something to the frame2
l.pack()

b1=Button(f1, fg="red", text="print now", command=func)               #for adding button    #command for adding some instruction using func
b1.pack(fill=X)
b2=Button(f2, fg="red", text="print now", command=func1)
b2.pack()
root.mainloop()
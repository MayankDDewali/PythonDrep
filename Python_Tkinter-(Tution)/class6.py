from tkinter import*
root=Tk()
count=0
def mayank(event):
    global count
    count+=1
    print(f"Hello I am Mayank {count}")

canvas_width=900                #for giving the positions
canvas_hight=500                #fro giving the positions

root.geometry(f"{canvas_width}x{canvas_hight}")

'''name="Mayank"                                #another mathod for using variable
print(f"your name is {name}")'''                #name is f-string

# can=Canvas(root,width=canvas_width,height=canvas_hight)
# can.pack()
# can.create_line(0,0,200,300,fill="black")             #for creating a line
# can.create_oval(400,200,200,400,fill="gray")                #for creating an oval
b1=Button(root,text="Click here")
b1.pack()
b1.bind('<Button-1>',mayank)

root.mainloop()
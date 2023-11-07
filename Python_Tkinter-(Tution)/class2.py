from tkinter import *
root=Tk()
root.title("Class-2")
root.geometry("1500x1000")
hello=Label(text='''Hello I am Mayank. Hello I am Mayank.
\n Hello I am Mayank. Hello I am Mayank. Hello I am
\n Mayank. Hello I am Mayank. Hello I am Mayank. Hello I am May
\nank. Hello I am Mayank. Hello I am Mayank. Hello I am Maya
\nnk. Hello I aHello Hello I am Mayank. Hello I 
\nam Mayank.  am Mayank. m Mayank. He
\nllo I am Mayank. Hello I am Mayank. H
\nello I am Mayank. ''',bg="gray",fg="black", padx=113, pady=80, font="comicsansms 25 bold", borderwidth=10, relief=GROOVE)
#sunken, groove, ridge, raise are 4 borders
hello.pack(anchor="n")
# hello.pack(anchor="e")                #east
# hello.pack(anchor="w")                #west
# hello.pack(anchor="ne")               #north-east
# hello.pack(anchor="nw")               #north-west
# hello.pack(side=BOTTOM,fill=Y)        #for bottom
root.mainloop()
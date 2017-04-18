from tkinter import *
from tkinter import ttk

root = Tk()
frame1=ttk.Frame(root)
frame1.pack()
frame1.config(height=200,width=200,relief=RIDGE, padding=(10,10))
ttk.Button(frame1,text="Click me frame 1").grid(row=0,column=0)
ttk.Button(frame1,text="Click me2 frame 1").grid(row=0,column=3)

frame2=ttk.Frame(root)
frame2.pack()
frame2.config(height=200,width=200,relief=RIDGE, padding=(10,10))
ttk.Button(frame2,text="Click me frame 2").pack()
ttk.Button(frame2,text="Click me 2 frame 2").pack()

ttk.LabelFrame(height=100,width=100,text="Thrid frame").pack()
root.mainloop()
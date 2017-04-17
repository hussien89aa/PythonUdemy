
from tkinter import *
from tkinter import ttk


root=Tk()
style=ttk.Style()
style.configure('TButton', background='#0B6CA3', font=('Arial',18))
entry=ttk.Entry(root,width=30)
entry.pack()
button=ttk.Button(root,text="Click Me!")
button.pack()
logo= PhotoImage(file="login.gif")
button.config(image=logo,compound=LEFT)
Resize_Logo=logo.subsample(10,10)
button.config(image=Resize_Logo)
def BuClick():
   print(entry.get())
   entry.delete(0,END)
   #entry.insert(0,"button clicked")

button.config(command=BuClick)

root.mainloop()
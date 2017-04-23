from tkinter import  *
from  tkinter import  ttk
root=Tk()

def key_press(event):
    print("tye:{}".format(event.type))

def button_press(event):
    print("button is press")
bu=ttk.Button(root,text="Click me")
bu.pack()
bu.bind("<ButtonPress>", button_press)
root.bind("<Control-c>",key_press)

root.mainloop()
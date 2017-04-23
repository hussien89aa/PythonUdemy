from tkinter import  *
from  tkinter import  ttk

def BuClick(id):
    print("Id:{}".format(id))


root=Tk()

ttk.Button(root,text="Click me 1" , command=lambda :BuClick(10)).pack()



root.mainloop()
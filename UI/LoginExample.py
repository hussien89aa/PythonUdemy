from  tkinter import *
from  tkinter import  ttk

root=Tk()
root.title("Login Page")
root.resizable(False,False)

l1=ttk.Label(root,text="User name:")
l1.grid(row=0,column=0)
etUserName=ttk.Entry(root,width=20)
etUserName.grid(row=0,column=1)
l2=ttk.Label(root,text="Password:")
l2.grid(row=1,column=0)
etPassword=ttk.Entry(root,width=20)
etPassword.grid(row=1,column=1)
etPassword.config(show="*")
Bulogin=ttk.Button(root,text="Login")
Bulogin.grid(row=2,column=1 )

def BuClick():
    print("User name:{}, Password: {}".format(etUserName.get(),etPassword.get()))

Bulogin.config(command=BuClick)


root.mainloop()
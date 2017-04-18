from tkinter import *
from tkinter import ttk

root=Tk()
style=ttk.Style()
style.theme_use('classic')
ttk.Label(root,text='Green',background='Green').grid(row=0,column=0,padx=5,pady=5,sticky='snew')
ttk.Label(root,text='Yellow',background='yellow').grid(row=0,column=1,ipadx=5,ipady=5 ,sticky='snew')
ttk.Label(root,text='Blue',background = 'Blue').grid(row=0,column=2, rowspan=2, sticky='snew')
ttk.Label(root,text='Orange',background='Orange').grid(row=1,column=0, columnspan=2, sticky='snew')

root.rowconfigure(0,weight=2)
root.rowconfigure(1,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=2)


root.mainloop()
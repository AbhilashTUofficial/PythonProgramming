import tkinter
from tkinter import *

window=tkinter.Tk();
window.geometry("300x400");
var=IntVar()
var.set(1)

def radioButtonClick():
    resultLabel=tkinter.Label(resultFrame,text="Option "+str(var.get())+" selected").pack();

frame=tkinter.LabelFrame(window,pady=30,padx=30);
resultFrame=tkinter.LabelFrame(window,padx=30,pady=30);
resultLabel=tkinter.Label(resultFrame,text="Option "+str(var.get())+" selected").pack();

# tkinter.Radiobutton(frame,text="Option 1",variable= var,value=1,command=radioButtonClick).grid(row=0,column=0);
# tkinter.Radiobutton(frame,text="Option 2",variable= var,value=2,command=radioButtonClick).grid(row=1,column=0);
# tkinter.Radiobutton(frame,text="Option 3",variable= var,value=3,command=radioButtonClick).grid(row=2,column=0);
for i in range(1,4):
    tkinter.Radiobutton(frame,text="Option "+str(i),variable=var,value=i,command=radioButtonClick).grid(row=i-1,column=0);
options=[
    ("4",4),
    ("5",5),
    ("6",6)
]
for opt,val in options:
    tkinter.Radiobutton(frame,text="Option "+opt,variable=var,value=val,command=radioButtonClick).grid(row=val-1,column=0);

frame.pack(padx=10,pady=10);
resultFrame.pack(pady=10,padx=10);
window.mainloop();
import tkinter
from tkinter.constants import SUNKEN

frame=tkinter.Tk();

label=tkinter.Label(frame,width=40,height=10,bg="#282828");
label.grid(row=0,column=0);

statusBar=tkinter.Label(frame,bg="#282828",fg="white",width=40,height=2,relief=SUNKEN);
statusBar.grid(row=1,column=0);

button1=tkinter.Button(statusBar,text="<<",fg="white",bg="#282828",padx=3,pady=3);
button1.grid(row=0,column=0);

button2=tkinter.Button(statusBar,text=">>",fg="white",bg="#282828",padx=3,pady=3);
button2.grid(row=0,column=3);

status=tkinter.Label(statusBar,text="STATUS",bg="#282828",fg="white",width=31);
status.grid(row=0,column=1,columnspan=2);

frame.mainloop();
import tkinter
from tkinter.constants import CENTER, E, N, SUNKEN, W

window=tkinter.Tk();

label=tkinter.Label(window,height=10,bg="#282828");
label.grid(row=0,column=0,sticky=W+E);

statusBar=tkinter.Label(window,bg="#282828",fg="white",height=2,relief=SUNKEN,);
statusBar.grid(row=1,column=0,sticky=W+E);

button1=tkinter.Button(statusBar,text="<<",fg="white",bg="#282828",padx=3,pady=3);
button1.grid(row=0,column=0);

button2=tkinter.Button(statusBar,text=">>",fg="white",bg="#282828",padx=3,pady=3);
button2.grid(row=0,column=3);

status=tkinter.Label(statusBar,text="STATUS",bg="#282828",fg="white",width=30,anchor=CENTER);
status.grid(row=0,column=1,columnspan=2);

window.mainloop();

import tkinter

window=tkinter.Tk();
myLabel1=tkinter.Label(window, text="First");
myLabel2=tkinter.Label(window, text="Second");
myLabel1.grid(row=0,column=0);
myLabel2.grid(row=1,column=1);

window.mainloop();
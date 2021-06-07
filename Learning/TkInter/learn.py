
import tkinter

root=tkinter.Tk();
myLabel1=tkinter.Label(root, text="First");
myLabel2=tkinter.Label(root, text="Second");
myLabel1.grid(row=0,column=0);
myLabel2.grid(row=1,column=1);

root.mainloop();
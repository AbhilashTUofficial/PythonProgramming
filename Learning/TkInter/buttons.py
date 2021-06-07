import tkinter
from tkinter.constants import DISABLED

frame=tkinter.Tk();
frame.title("Buttons");

def clickFunc():
    tkinter.Label(frame,text="Button Clicked!").pack();

b1=tkinter.Button(frame,text="Button 1");
b2=tkinter.Button(frame,text="Button 2",state=DISABLED);
b3=tkinter.Button(frame,text="Button 3",padx=60,fg="red");
b4=tkinter.Button(frame,text="Button 4",pady=60,bg="#ffbf00");
b5=tkinter.Button(frame,text="Button 5",padx=30,pady=30);
b6=tkinter.Button(frame,text="Button 6",command=clickFunc);

b1.pack();
b2.pack();
b3.pack();
b4.pack();
b5.pack();
b6.pack();

frame.mainloop();
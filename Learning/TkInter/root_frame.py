from tkinter import *
from PIL import ImageTk,Image


window=Tk();
window.title("Frames");
window.geometry("300x300");

frameOne=LabelFrame(window,text="Frame 1",padx=10,pady=10);
frameTwo=LabelFrame(window,text="Frame 2",padx=10,pady=10);

labelA=Label(frameOne,text="label 1");
labelA.grid(row=0,column=0,padx=10,pady=10);
labelB=Label(frameOne,text="label 2");
labelB.grid(row=0,column=1,padx=10,pady=10);
labelC=Label(frameOne,text="label 3");
labelC.grid(row=1,column=0,padx=10,pady=10);
labelD=Label(frameOne,text="label 4");
labelD.grid(row=1,column=1,padx=10,pady=10);

labelA=Label(frameTwo,text="label 1");
labelA.grid(row=0,column=0,padx=10,pady=10);
labelB=Label(frameTwo,text="label 2");
labelB.grid(row=0,column=1,padx=10,pady=10);
labelC=Label(frameTwo,text="label 3");
labelC.grid(row=1,column=0,padx=10,pady=10);
labelD=Label(frameTwo,text="label 4");
labelD.grid(row=1,column=1,padx=10,pady=10);

frameOne.pack(pady=10,padx=10);
frameTwo.pack(pady=10,padx=10);

window.mainloop();
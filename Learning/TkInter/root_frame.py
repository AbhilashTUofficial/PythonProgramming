from tkinter import *
from PIL import ImageTk,Image


frame=Tk();
frame.title("Frame");
frame.geometry("400x400");

img=ImageTk.PhotoImage(Image.open('Learning/TkInter/pycharm.png'))

label=Label(image=img)
label.pack()
frame.mainloop();
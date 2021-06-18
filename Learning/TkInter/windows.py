import tkinter
from PIL import ImageTk,Image


window1=tkinter.Tk();
window1.title("Window 1");
window1.geometry("300x300");

def openWin2():
    global img;
    window2=tkinter.Toplevel();
    window2.title("Window 2");
    window2.geometry("300x330");
    img=ImageTk.PhotoImage(Image.open('Img/pycharm.png').resize((300,300)));
    tkinter.Label(window2,image=img).pack();
    tkinter.Label(window2,text="Window 2").pack();



button=tkinter.Button(window1,text="Open Second Window",command=openWin2).pack();
tkinter.Label(window1,text="Window 1").pack();

window1.mainloop();
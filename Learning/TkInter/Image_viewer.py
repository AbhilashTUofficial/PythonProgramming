import tkinter
from PIL import ImageTk,Image

frame=tkinter.Tk();
frame.title("Images");
# frame.geometry("600x600");
pyimage1=ImageTk.PhotoImage(Image.open('Img/pycharm.png').resize((400,400)));
pyimage2=ImageTk.PhotoImage(Image.open('Img/python.png').resize((400,400)));
pyimage3=ImageTk.PhotoImage(Image.open('Img/vscode.png').resize((400,400)));
# pyimage4=ImageTk.PhotoImage(Image.open('Img/pycharm.png').resize((400,400)));

imagesList=[pyimage1,pyimage2,pyimage3];
label=tkinter.Label(image=imagesList[1]);
label.grid(row=0,column=0,columnspan=3);

def backward(n):
    global label;
    global forwardButton;
    global backwardButton;
    try:
        label.grid_forget();
        label=tkinter.Label(image=imagesList[n-1]);
        label.grid(row=0,column=0,columnspan=3);
        forwardButton=tkinter.Button(frame,text=">>",command=lambda : forward(n-1));
        backwardButton=tkinter.Button(frame,text="<<",command=lambda : backward(n+1));
        backwardButton.grid(row=1,column=0);
        forwardButton.grid(row=1,column=2);
    except:
        label.grid_forget();
        label=tkinter.Label(image=imagesList[0]);
        label.grid(row=0,column=0,columnspan=3);
        backwardButton=tkinter.Button(frame,text="<<",command=lambda : backward(0));
        forwardButton=tkinter.Button(frame,text=">>",command=lambda : forward(0));

        backwardButton.grid(row=1,column=0);
        forwardButton.grid(row=1,column=2);
    

def forward(n):
    global label;
    global forwardButton;
    global backwardButton;
    try:
        label.grid_forget();
        label=tkinter.Label(image=imagesList[n+1]);
        label.grid(row=0,column=0,columnspan=3);
        forwardButton=tkinter.Button(frame,text=">>",command=lambda : forward(n+1));
        backwardButton=tkinter.Button(frame,text="<<",command=lambda : backward(n-1));
        backwardButton.grid(row=1,column=0);
        forwardButton.grid(row=1,column=2);
    except:
        label.grid_forget();
        label=tkinter.Label(image=imagesList[0]);
        label.grid(row=0,column=0,columnspan=3);
        backwardButton=tkinter.Button(frame,text="<<",command=backward);
        forwardButton=tkinter.Button(frame,text=">>",command=lambda : forward(0));

        backwardButton.grid(row=1,column=0);
        forwardButton.grid(row=1,column=2);

backwardButton=tkinter.Button(frame,text="<<",command=lambda : backward(1));
forwardButton=tkinter.Button(frame,text=">>",command=lambda : forward(1));

backwardButton.grid(row=1,column=0);
forwardButton.grid(row=1,column=2);

frame.mainloop();
import tkinter
from PIL import ImageTk,Image

frame=tkinter.Tk();
frame.title("Images");
# frame.geometry("600x600");
img1=ImageTk.PhotoImage(Image.open('Img/pycharm.png').resize((400,400)));
img2=ImageTk.PhotoImage(Image.open('Img/python.png').resize((400,400)));
img3=ImageTk.PhotoImage(Image.open('Img/vscode.png').resize((400,400)));
img4=ImageTk.PhotoImage(Image.open('Img/pycharm.png').resize((400,400)));

imagesList=[img1,img2,img3,img4];
n=0;
label=tkinter.Label(image=img1);
label.grid(row=0,column=0,columnspan=3);

def backward():
    pass

def forward():
    label=tkinter.Label(image=imagesList[2]);
    label.grid(row=0,column=0,columnspan=3);
    





backwardButton=tkinter.Button(frame,text="<<",command=backward);
forwardButton=tkinter.Button(frame,text=">>",command=lambda : forward());

backwardButton.grid(row=1,column=0);
forwardButton.grid(row=1,column=2);

frame.mainloop();
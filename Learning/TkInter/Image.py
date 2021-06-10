import tkinter
from PIL import ImageTk,Image

frame=tkinter.Tk();
frame.title("Images");
frame.geometry("400x400");
img=ImageTk.PhotoImage(Image.open('Img/pycharm.png').resize((500,500)))

label=tkinter.Label(image=img);
label.pack();
frame.mainloop();
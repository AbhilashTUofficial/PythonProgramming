import tkinter
from PIL import ImageTk,Image

window=tkinter.Tk();
window.title("Images");
window.geometry("400x400");
img=ImageTk.PhotoImage(Image.open('Img/pycharm.png').resize((500,500)))

label=tkinter.Label(image=img);
label.pack();
window.mainloop();
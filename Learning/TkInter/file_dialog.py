import tkinter
from tkinter import filedialog

window=tkinter.Tk();
window.title("File Open Dialog");
window.geometry("400x400");


def OpenFile():
    window.file_path=filedialog.askopenfile(
        initialdir="/home/abhilash/Downloads",
        title="Select file",
        filetypes=(("PNG files","*.png"),("JPG files","*.jpg")));
    tkinter.Label(window,text=window.file_path).pack();

tkinter.Button(text="Open File Manager",command=OpenFile).pack();

window.mainloop();

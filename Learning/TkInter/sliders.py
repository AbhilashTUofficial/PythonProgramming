import tkinter
from tkinter.constants import HORIZONTAL

window=tkinter.Tk();
window.title("Slider");
window.geometry("200x200");

def changeValue(value):
    # string=window.geometry();
    # hori=slice(0,3);
    # vert=slice(4,7)
    # horiSlider.set(int(hori));
    tkinter.Label(text=str(horiSlider.get())+"X"+str(vertSlider.get())).pack();
    window.geometry(str(horiSlider.get())+"x"+str(vertSlider.get()));   

horiSlider=tkinter.Scale(window,from_=200,to=400,orient=HORIZONTAL,command=changeValue);
vertSlider=tkinter.Scale(window,from_=200,to=400,orient=HORIZONTAL,command=changeValue);
horiSlider.pack();
vertSlider.pack();
tkinter.Button(text="Change Geometry",command=lambda:changeValue(0)).pack();
tkinter.Label(text="200X200").pack();

window.mainloop();

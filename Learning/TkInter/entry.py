import tkinter

frame=tkinter.Tk();
frame.title("Entry")

def clickFunc():
    tkinter.Label(frame,text=inputField.get()).pack();

inputField=tkinter.Entry(frame,width=30,bg="#d3d3d3",fg="#696969",highlightcolor="#ffbf00");
inputField.insert(0,"Enter the text");
inputField.pack();
button=tkinter.Button(frame,text="Print",command=clickFunc).pack();


frame.mainloop();
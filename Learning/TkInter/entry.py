import tkinter

window=tkinter.Tk();
window.title("Entry")

def clickFunc():
    tkinter.Label(window,text=inputField.get()).pack();

inputField=tkinter.Entry(window,width=30,bg="#d3d3d3",fg="#696969",highlightcolor="#ffbf00");
inputField.insert(0,"Enter the text");
inputField.pack();
button=tkinter.Button(window,text="Print",command=clickFunc).pack();


window.mainloop();
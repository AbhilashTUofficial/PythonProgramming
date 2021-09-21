import tkinter

window=tkinter.Tk();
window.title("Fonts")
Font_tuple = ("Comic Sans MS", 20, "bold");

def clickFunc():
    displayText=tkinter.Label(window,text=inputField.get());
    displayText.config(font=Font_tuple);
    displayText.pack();

inputField=tkinter.Entry(window,width=30,bg="#d3d3d3",fg="#696969",highlightcolor="#ffbf00");
inputField.insert(0,"Enter the text");
inputField.pack();
button=tkinter.Button(window,text="Print",command=clickFunc).pack();


window.mainloop();
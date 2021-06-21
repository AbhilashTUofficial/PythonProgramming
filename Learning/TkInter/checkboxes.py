import tkinter
from tkinter import BooleanVar, IntVar, StringVar
from tkinter.constants import E, W


window=tkinter.Tk();
window.title("Check Boxes");
window.geometry("200x200");

checkOne=IntVar();
checkTwo=IntVar();
checkThree=BooleanVar();
checkFour=StringVar();

tkinter.Checkbutton(text="CheckBox One",variable=checkOne,width=30,anchor=W).pack();
tkinter.Checkbutton(text="CheckBox Two",variable=checkTwo,width=30,anchor=W).pack();
tkinter.Checkbutton(text="CheckBox Three",variable=checkThree,width=30,anchor=W).pack();
checkBoxFour=tkinter.Checkbutton(text="CheckBox Four",variable=checkFour,onvalue="Yes",offvalue="No",width=30,anchor=W);
checkBoxFour.deselect();
checkBoxFour.pack();

window.mainloop();
import tkinter
from tkinter import messagebox
import math

window=tkinter.Tk();
window.title("Message Box");
window.geometry("400x400");

def showInfo():
    messagebox.showinfo("Show Info Pop Up","Information");

def showError():
    messagebox.showerror("Show Error Pop Up","Error");

def askQuestion():
    messagebox.askquestion("Ask Question Pop Up","Question");

def askOkCancel():
    messagebox.askokcancel("Ask Ok Cancel Pop Up","OK OR CANCEL");

def askYesNo():
    messagebox.askyesno("Ask Yes No Pop Up","YES OR NO");

def askRetryCancel():
    messagebox.askretrycancel("Ask Retry Cancel Pop Up","RETRY OR CANCEL");

def guessTheNumber(arr):
    arr1=arr[:round(len(arr)/2)]
    arr2=arr[round(len(arr)/2):]    
    n=0;
    if(len(arr)==1):
        n=arr[0];
    
    if(n==0):
        res=messagebox.askyesno("","Is your number one of the following? \n"+str(arr1));

        if(res==1):
            guessTheNumber(arr1);
        else:
            guessTheNumber(arr2);
    else:
        messagebox.showinfo("Found your Number","Your Number is "+str(n));


frame=tkinter.LabelFrame(window,padx=10,pady=10,bg="#ffbf00");
tkinter.Button(frame,text="Show Info",width=16,padx=5,pady=5,command=showInfo).pack();
tkinter.Button(frame,text="Show Warning",width=16,padx=5,pady=5,command=lambda : messagebox.showwarning("Show Warning Pop Up","Warnings")).pack();
tkinter.Button(frame,text="Show Error",width=16,padx=5,pady=5,command=showError).pack();
tkinter.Button(frame,text="Ask Question",width=16,padx=5,pady=5,command=askQuestion).pack();
tkinter.Button(frame,text="Ok or Cancel",width=16,padx=5,pady=5,command=askOkCancel).pack();
tkinter.Button(frame,text="Ok or Cancel",width=16,padx=5,pady=5,command=askOkCancel).pack();
tkinter.Button(frame,text="Yes or No",width=16,padx=5,pady=5,command=askYesNo).pack();
tkinter.Button(frame,text="Yes No or Cancel",width=16,padx=5,pady=5,command=lambda : messagebox.askyesnocancel("Ask Yes No Cancel Pop Up","YES NO OR CANCEL")).pack();
tkinter.Button(frame,text="Retry Or Cancel",width=16,padx=5,pady=5,command=askRetryCancel).pack();
tkinter.Button(frame,text="GUESS THE NUMBER",width=16,padx=5,pady=5,command=lambda : guessTheNumber([1,2,3,4,5,6,7,8,9])).pack();


frame.pack(pady=10,padx=10);
window.mainloop();
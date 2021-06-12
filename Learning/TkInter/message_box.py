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

def guessTheNumber(l,m):
    print(l,m)
    n=math.floor(l+m/2);
    if(l+1==m):
        messagebox.showinfo("Found your Number","Your Number is "+str(n));
    else: 
        res=messagebox.askyesno("Guess A Number (1-9)","Your Number is between "+str(l)+" and "+str(m));
        n=round(m/2)
        if(res==1):
            guessTheNumber(l,n)
        elif(res==0):
            guessTheNumber(n,m)

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
tkinter.Button(frame,text="GUESS THE NUMBER",width=16,padx=5,pady=5,command=lambda : guessTheNumber(1,9)).pack();


frame.pack(pady=10,padx=10);
window.mainloop();
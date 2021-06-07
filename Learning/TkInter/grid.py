import tkinter

frame=tkinter.Tk();
frame.title("Grid");

for r in range(3):
    for c in range(3):
        rc=tkinter.Label(frame,text=f"Row-{r} Col-{c}" ).grid(row=r,column=c);
        

# r0c0=tkinter.Label(frame,text="Row-0 Col-0");
# r0c1=tkinter.Label(frame,text="Row-0 Col-1");
# r0c2=tkinter.Label(frame,text="Row-0 Col-2");
# r1c0=tkinter.Label(frame,text="Row-1 Col-0");
# r1c1=tkinter.Label(frame,text="Row-1 Col-1");
# r1c2=tkinter.Label(frame,text="Row-1 Col-2");
# r2c0=tkinter.Label(frame,text="Row-2 Col-0");
# r2c1=tkinter.Label(frame,text="Row-2 Col-1");
# r2c2=tkinter.Label(frame,text="Row-2 Col-2");

# r0c0.grid(row=0,column=0);
# r0c1.grid(row=0,column=1);
# r0c2.grid(row=0,column=2);
# r1c0.grid(row=1,column=0);
# r1c1.grid(row=1,column=1);
# r1c2.grid(row=1,column=2);
# r2c0.grid(row=2,column=0);
# r2c1.grid(row=2,column=1);
# r2c2.grid(row=2,column=2);


frame.mainloop();
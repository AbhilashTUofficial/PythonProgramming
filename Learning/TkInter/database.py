import tkinter
import sqlite3
from tkinter import *;


window=tkinter.Tk();
window.title("DataBase");
connection=sqlite3.connect("database.db");

request=connection.cursor();


# request.execute("""CREATE TABLE database_table(
#     column1 text,
#     column2 text,
#     column3 integer
#     )""");

def updateDb():
    global c1r1;

    connection=sqlite3.connect("database.db");
    request=connection.cursor();

    request.execute("INSERT INTO database_table VALUES (:column1,:column2,:column3)",
    {
        'column1':c1r1.get()
    }
    )

    connection.commit();
    connection.close();

# GUI

tkinter.Label(window,text="No.",width=5).grid(column=0,row=0,padx=5,pady=5);
tkinter.Label(window,text="Column 1",width=8).grid(column=1,row=0,padx=5,pady=5);
tkinter.Label(window,text="Column 2",width=8).grid(column=2,row=0,padx=5,pady=5);
tkinter.Label(window,text="Column 3",width=8).grid(column=3,row=0,padx=5,pady=5);



for r in range(1,5):
    tkinter.Label(window,text=str(r),width=5).grid(column=0,row=r,pady=5,padx=5);

c1r1=tkinter.Entry(window,width=20).grid(row=1,column=1,padx=10,pady=5);
c1r2=tkinter.Entry(window,width=20).grid(row=2,column=1,padx=10,pady=5);
c1r3=tkinter.Entry(window,width=20).grid(row=3,column=1,padx=10,pady=5);
c1r4=tkinter.Entry(window,width=20).grid(row=4,column=1,padx=10,pady=5);

c2r1=tkinter.Entry(window,width=20).grid(row=1,column=2,padx=10,pady=5);
c2r2=tkinter.Entry(window,width=20).grid(row=2,column=2,padx=10,pady=5);
c2r3=tkinter.Entry(window,width=20).grid(row=3,column=2,padx=10,pady=5);
c2r4=tkinter.Entry(window,width=20).grid(row=4,column=2,padx=10,pady=5);

c3r1=tkinter.Entry(window,width=20).grid(row=1,column=3,padx=10,pady=5);
c3r2=tkinter.Entry(window,width=20).grid(row=2,column=3,padx=10,pady=5);
c3r3=tkinter.Entry(window,width=20).grid(row=3,column=3,padx=10,pady=5);
c3r4=tkinter.Entry(window,width=20).grid(row=4,column=3,padx=10,pady=5);


tkinter.Button(window,text="UPDATE TO DATABASE !",command=updateDb).grid(row=5,column=0,columnspan=4,pady=20,ipadx=80);


connection.commit();
connection.close();

window.mainloop();
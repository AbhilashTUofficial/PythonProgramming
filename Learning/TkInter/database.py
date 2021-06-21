import tkinter
import sqlite3


window=tkinter.Tk();
window.title("DataBase");
window.geometry("200x200");

connection=sqlite3.connect("database.db");

request=connection.cursor();



request.execute("""CREATE TABLE database_table(
    column1 text,
    column2 text,
    column3 integer
    )""");

connection.commit();
connection.close();


window.mainloop();
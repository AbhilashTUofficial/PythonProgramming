import tkinter

window=tkinter.Tk();
window.title("Dropdown");
window.geometry("200x200");

selectedOne=tkinter.StringVar();
selectedOne.set("Menu1");
tkinter.OptionMenu(window,selectedOne,"MenuItem 1","MenuItem 2","MenuItem 3").pack();

selectedTwo=tkinter.IntVar();
selectedTwo.set(0);

menuItems=[
    4,3,2,1
];
# The * Separate each items on the list.
tkinter.OptionMenu(window,selectedTwo,*menuItems).pack();

window.mainloop();
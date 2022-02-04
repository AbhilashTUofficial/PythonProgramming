# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# def window():
#    app = QApplication(sys.argv)
#    w = QWidget()
#    b = QLabel(w)
#    b.setText("Hello World!")
#    w.setGeometry(100,100,200,50)
#    b.move(50,20)
#    w.setWindowTitle("PyQt5")
#    w.show()
#    sys.exit(app.exec_())
# if __name__ == '__main__':
#    window()



class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i

    def add(x,y):
        return(x.real+y.real,x.imaginary+y.imaginary)

def display(c):
    print("Complex number 1 :", c[0] ,"+ i" + str(c[0]))
    print("Complex number 2 :", c[1], "+ i" + str(c[1]))




c1=Complex(3,2)
c2=Complex(9,5)



res=Complex.add(c1,c2)
display(res)
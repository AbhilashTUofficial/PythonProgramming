import time
from multiprocessing import Process



def process():

    for i in range(60):
        time.sleep(1)
        open('Learning/Intermediate/LoadingBar/file.txt',"w").write(f'{i}')

def readProgress():
    for i in range(30):
        time.sleep(2)
        print(open('Learning/Intermediate/LoadingBar/file.txt',"r").read()) 


def basic():

    pass

    




if __name__=="__main__":
    basic()
    p1=Process(target=process())
    p2=Process(target=readProgress())
    p1.start()

    p2.start()

    

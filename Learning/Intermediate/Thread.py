from threading import Thread
from time import sleep
import time

#* Threads: An entity within a process that can be scheduled (also know as lightweight process)
#
# A process can spawn multiple threads.
# All threads within a process share the same memory.
# lightweight
# Starting a thread is faster than starting a process
# Great for I/O-bound tasks.
# 
# Threading is limited by GIL: Only one thread at a time.
# No effect for CPU-bound tasks.
#! Not interruptable / killable.
#! Careful with race conditions.
# Race conditions: when two or more threads try to modify a same variable.

#* GIL : Global Interpreter Lock
# A lock that allows only one thread at a time to execute in python
# Needed in Cpython because memory management is not thread-safe
#! Avoid 
#!   - Use multiprocessing
#!   - Use a different, free-threaded Python implementation( Jython, IronPython)
#!   - Use Python as a wrapper for third-party libraries (C/C++ -> numpy, scipy)


def _task(t,_):

    for num in range(10):
        sleep(1)
        print(f"Thread {t}: {num}",)
    
def _multiThreading():
    #! Don't use () on target
    #! Use args=value to pass arguments
    for t in range(3):
        thread=Thread(target=_task,args=(t,0))
        thread.start()
        # thread.join()  

#* Passing data between threads.

x=0
def increament():
    global x
    x+=1


def passingData():

    print(f"Initial Value: {x}")

    thread1=Thread(target=increament)
    thread2=Thread(target=increament)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"Final Value: {x}")




def main():
    passingData()
    # _multiThreading()
        

if __name__=='__main__':
    main()

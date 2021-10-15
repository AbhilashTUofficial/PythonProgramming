from threading import Thread
import datetime
from time import sleep

# Process: An instance of a program (e.g a Python interpreter)
#
# Takes advantage of multiple CPUs and cores.
# Separate memory space -> Memory is not shared between processes.
# Great for PU-bound processing.
# New process is  started independently from other processes.
# Processes are interruptable / killable.
# One GIL for each process -> Avoids GIL limitation
#
# Use more memory
# Starting a process is slower than starting a thread.
# Use more resourcess.
# IPC (inter-process communication) is more complicated.

# Threads: An entity within a process that can be scheduled (also know as lightweight process)
#
# A process can spawn multiple threads.
# All threads within a process share the same memory.
# lightweight
# Starting a thread is faster than starting a process
# Great for I/O-bound tasks.
# 
# Threading is limited by GIL: Only one thread at a time.
# No effect for CPU-bound tasks.
# Not interruptable / killable.
# Careful with race conditions.
# Race conditions: when two or more threads try to modify a same variable.


def main():

    def threadOne():
        for _ in range(10):
            sleep(1)
            print("Thread One: ", datetime.datetime.now().second)


    def threadTwo():
        for _ in range(10):
            sleep(1)
            print("Thread Two: ", datetime.datetime.now().second)


    def threadThree():
        for _ in range(10):
            sleep(1)
            print("Thread Three: ", datetime.datetime.now().second)

    #! Don't use () on target
    #! Use args=value to pass arguments


    Thread(target=threadOne).start()
    Thread(target=threadTwo).start()
    Thread(target=threadThree).start()

if __name__=='__main__':
    main()

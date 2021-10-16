
# Process: An instance of a program (e.g a Python interpreter)
#
# Takes advantage of multiple CPUs and cores.
#! Separate memory space -> Memory is not shared between processes.
# Great for PU-bound processing.
# New process is  started independently from other processes.
# Processes are interruptable / killable.
# One GIL for each process -> Avoids GIL limitation
#
# Use more memory
# Starting a process is slower than starting a thread.
# Use more resourcess.
# IPC (inter-process communication) is more complicated.

from multiprocessing import Process
import os
import time

processes=[]
cpuCores=os.cpu_count()

def _task(n,_):
    for num in range(10):
            time.sleep(1)
            print(f"Process {n}: {num}")

#? This function work on all core of the CPU
#? at the same time, hence multiProcessing.
def _multiProcessing():
    #* Create Processes.
    for core in range(cpuCores):
        p=Process(target=_task,args=(core,0))
        processes.append(p)

    #* Start Processes.
    for p in processes:
        p.start()

    #* Join Processes, means hold other processes.
    for  p in processes:
        p.join()

#? This function work on only one core at a time
#? hence singleProcessing
def _singleProcessing():
    #* Create Processes.
    for core in range(cpuCores):
        p=Process(target=_task,args=(core,0))
        #* Start Processes.
        p.start()
        #* Join Processes.
        p.join()

#? This function allows difference process to access
#? same memory location.
#! This function will fail.
#! increaseByOne function is intended to increment the 
#! the value of x in seperate process.
#! Every process create it's own version of the same variable,
#! this is why process use more momery and slow.
def failProcess():
    x=0
    #* Create Processes.
    for core in range(cpuCores):
        p=Process(target=increaseByOne,args=(core,x))
        #* Start Processes.
        p.start()
        #* Join Processes.
        p.join()
def increaseByOne(c,x):
    print(f"Process: {c} x: {x}")
    x+=1
    time.sleep(1)



def main():

    _multiProcessing()
    # _singleProcessing()
    # failProcess()
    print("All Processes Ended.")


if __name__=='__main__':
    main()
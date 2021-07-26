from threading import Thread
import datetime
from time import sleep


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

from os import system,name
import string
from time import sleep
import random


def clear():
    # for windows
    if name == 'nt':_ = system('cls')
    # for mac and linux
    else: _ = system('clear')

def findAscii(s):
    if len(s)==1:return ord(s)
    result=''
    for i in s:
        result=f'{result}{ord(i)}'
    return result
    

def colorize(arr):
    color=['\033[95m','\033[94m','\033[92m','\033[93m','\033[91m']
    c=random.randint(0, len(color)-1)
    s=''
    for i in arr:
        s=f"{s}{color[c]}{i}"
    return s


def main():
    
    i,letters,finalStr=0,[' ','!'],'Hello World!!!'
    [letters.append(_) for _ in string.ascii_letters]
    tmpStr=f'{letters[0]}'

    cl='\033[95m'
    color=['\033[95m','\033[94m','\033[92m','\033[93m','\033[91m']
    c=random.randint(0, len(color)-1)

    while True:
        clear()
        # s=[f'{color[random.randint(0, len(color)-1)]}{s}' for s in tmpStr]
        [print(x,end='')for x in tmpStr]
        # print(f"{color[1]}{tmpStr}{color[1]}")
        sleep(0.1)
        if findAscii(tmpStr)==findAscii(finalStr):break
        if(findAscii(tmpStr[-1])==findAscii(finalStr[len(tmpStr)-1])):
            tmpStr=f'{tmpStr}{letters[i]}'
            i=0
        else:
            tmpStr=f'{tmpStr[:-1]}{letters[i]}'
            i+=1

    
if __name__=="__main__":
    main()
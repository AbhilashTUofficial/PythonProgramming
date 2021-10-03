import time
import sys
# Generators are functions which return object to iterate over.
# Memory efficient.


# Initialisation

def funcGenerator():
    yield 1
    yield 2
    yield 3

def numberGenerator():
    for i in range(1,5):
        yield i
    yield 6
    yield 7

print(numberGenerator)

def functionOne(n=numberGenerator()):
    print('First number : ',next(n))
    print('Second number : ',next(n))

    n=numberGenerator()
    for i in numberGenerator():
        print('Number ',i+next(n))

n=numberGenerator()
def operations(n):
    print(sum(n))
    x=[]
    for i in numberGenerator():
        x.insert(0,i)
    

def sec():
    for i in range(10):
        yield i

n=sec()

def secCounter():
    for i in sec():
        print(i)
        time.sleep(1)

def arrayObj():
    num=[]
    for i in range(100):
        num.append(i)
    return num

def generatorObj():
    for i in range(100):
        yield i

def sizeOf():
    print(sys.getsizeof(arrayObj()))
    print(sys.getsizeof(generatorObj()))

def fib(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b

def fib2(limit):
    a,b=0,1
    while a<limit:
        print(a)
        a,b=b,b+a
        a=b
        

# fib2(1000000)
# for i in fib(50):
#     print(i)


from math import isqrt

def primeLessThan(n :int):
    
    if n<=2:return []

    isPrime=[True]*n
    isPrime[0],isPrime[1]=False,False

    for i in range(2,isqrt(n)):
        if isPrime[i]:
            for x in range(i*i,n,i):
                isPrime[x]=False
    
    return [i for i in range(n) if isPrime[i]]


def main():
    print(primeLessThan(100))


if __name__=="__main__":
    main()
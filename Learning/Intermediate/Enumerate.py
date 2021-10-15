
#! Enumerate return the index and the values as a tuple,
#! this is useful when we need to access both value and index.

def main():
    x=[1,6,4,2,6,3,0]
    for idx,val in enumerate(x):
        if(idx %2==0):
            x[idx]+=val
    print(x)

    dictionary={}
    for idx,val in enumerate(x):
        dictionary[idx]=val
    print(dictionary)



if __name__=='__main__':
    main()
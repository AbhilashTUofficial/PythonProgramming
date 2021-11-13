


def main():
    arr1=[True,True,True]
    arr2=[True,False,False]
    arr3=[2,4,5]


    if all(arr1):
        print(f'{arr1} is True')
    if any(arr2):
        print(f'{arr2} is True')

    if all(arr3)%2==0:
        print(f'{arr3} is even')

    print(all([True if i%2==0 else False for i in arr3]))
    
    arr=[2, 3, 4, 5, 6]
    print(len(arr))

if __name__=='__main__':
    main()
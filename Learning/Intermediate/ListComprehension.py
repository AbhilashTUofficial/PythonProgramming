
#! syntax: 
# create list -> [for variable in iterable]
# filter      -> [expression for variable in iterable if-condition]
# modify      -> [expression if-else-condition for variable in iterable]

def main():

    # Convert long digit into individual digits.
    n=1244
    print([int(_) for _ in str(n)]) 
    # to get array with no repeating elements.
    arr0=[1,2,2,3,4,4,4,5]
    arr1=[]
    [arr1.append(x)for x in arr0 if x not in arr1]

    # Function in list comprehension.
    def cube(i):
        return i*i*i
    print([cube(i)for i in arr0 if i<4])
    print([0 if i%2==0 else i for i in arr0])
    dictA={i:val for i,val in enumerate(arr0)}
    print(dictA)

    # 2D array
    arr2=[1,2,3]
    print([ [] for _ in arr2])
    print([[i for i in arr2]for _ in arr2])


# 2D looping
arr=[]
[arr.append(i,j) for i in arr for j in arr]
[arr.append(i,j) for i in arr for j in arr if arr!=[]]


if __name__=='__main__':
    main()
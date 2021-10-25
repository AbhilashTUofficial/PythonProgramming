
# to get array with no repeating elements.
arr0=[1,2,2,3,4,4,4,5]
arr1=[]
[arr1.append(x)for x in arr0 if x not in arr1]
#! Or Convert into a set
#! A set is an unorder colloction of unique elements.
# print(arr1)

# to get (i,j),(i+j),(i!=j), etc combination of a array.
# print([(i,j) for i in arr1 for j in arr1])

m={3:'3',2:'b'}
m=sorted(m)
print(m[-1])

# Inline-if statements
# print("statement1" if(condition) else "statement1")

a=4
print("Even" if(a%2==0)else "Odd");

# Combine,reverse and swap case

sentence="pROGRAMMING pYTHON"
print(' '.join(reversed((sentence.swapcase()).split(' '))))

# Convert long digit into individual digits.
n=1244
print([int(_) for _ in str(n)])

# Check the value is the given instance
print(isinstance("string",str))

# Flatten nested Array
def flattenArray(arr):
    arr2=[]
    for i in arr:
        if(isinstance(i,int)):
            arr2.append(i)
        else:
            arr2.extend(flattenArray(i))
    return arr2

# Remove a specific element from array
arr=[]
arr=[i for i in arr if i!=0]

# Find the ascii value
print(ord('s'))

# Reversed range in loop
for i in range(10)[::-1]:
    pass


# Get a array of unique elements and 
# a array of its count
arr=[1,4,4,2,2,3,7]
arr=sorted(arr)
arrY,arrX=[],[]
[arrX.append(_) for _ in arr if _ not in arrX]
[arrY.append(arr.count(_)) for _ in arrX]
# Most frequent elements
arrX[arrY.index(max(arrY))]
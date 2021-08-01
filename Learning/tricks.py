
# to get array with no repeating elements.
arr0=[1,2,2,3,4,4,4,5]
arr1=[]
[arr1.append(x)for x in arr0 if x not in arr1]
# print(arr1)

# to get (i,j),(i+j),(i!=j), etc combination of a array.
# print([(i,j) for i in arr1 for j in arr1])

m={3:'3',2:'b'}
m=sorted(m)
print(m[-1])
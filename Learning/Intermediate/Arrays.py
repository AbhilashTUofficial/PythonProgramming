import sys
# List or arrays: ordered, mutable allows duplicate elements.

# Initialisation
listA=["one",2,True];
# fist element in the list
listA[0];
# last element in the list
listA[-1];
# second-last element in the list
listA[-2];
# smallest and largest element
min([6,4,3,2])
max([6,4,3,2])

# iterate through list-item
for item in listA:
    pass;
# check the items in the list
if "one" in listA:
    pass;
# get the length of the list
len(listA);
len([1,2,3])
# Append new item to list
listA.append("new element");
# Insert new item to list
listA.insert(0,"new element");
# Pop item from list
listA.pop(); # pop() return the popped item back.
# Remove item from list
listA.remove(True);
# Clear list
listA.clear();
# Reverse the list
listA.reverse();
# Sort the list
listA.sort();
# Sorted copy of the original list
sorted(listA);
# Create a list with same element multiple times.
listA=[1]*3;
# Create a list from another list
listB=[3+i*i for i in listA]
# Concatenage a new list
listC=listA+listB;
# Slice the list by interval
listC[2:5];
# Slice the list from begining
listC[:5];
# Slice the list to end
listC[2:];
# Slice the list from begining to end
listC[:];
# Slice the list by step
listC[::2];
listC[::1];
listC[::-1] # Reverse the list.
# Copy the list
listD=listC.copy();
# Convert tuple to list
tupleA=(1,2,3)
listF=list(tupleA);
# Un-packing the list
elem1,elem2,elem3=listA;
listG=[1,2,3,4,5,6];
elem4,*elemX,elem9=listG;
# Merge elements from another list
listG.extend(listA)

print(sys.getsizeof(listA)); # 80 bytes

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


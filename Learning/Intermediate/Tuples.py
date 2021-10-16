import sys
# Tuple: ordered, immutable, allows duplicate elements.

# Initialisation
tupleA=("one",2,True);
tupleB=("three",);
# Create tuple from a list
tupleC=tuple([1,2,3,4]);
tupleD=tuple([i+1 for i in tupleC])
# fist element in the tuple
tupleC[0];
# last element in the tuple
tupleC[-1];
# second-last element in tuple
tupleC[-2];
# iterate through tuple-item
for i in tupleC:
    pass;
# check the items in the tuple
if "one" in tupleA:
    pass;
# Count the items in the tuple
tupleC.count(1);
# Return the index of item.
tupleC.index(1);
# Convert list to tuple.
listA=[1,2,3,4];
tupleE=tuple(listA);
# Slice the tuple by interval
tupleC[2:5];
# Slice the tuple from begining
tupleC[:5];
# Slice the tuple to end
tupleC[2:];
# Slice the tuple from begining to end
tupleC[:];
# Slice the tuple by step
tupleC[::2];
tupleC[::1];
tupleC[::-1] # Reverse the tuple.
# Un-pack the tuple.
(i,j,k)=(1,2,3) # i=1,j=2,k=3
tupleF=(1,2,3);
elem1,elem2,elem3=tupleF;
tupleG=(1,2,3,4,5,6);
elem4,*elemX,elem9=tupleG;

print(sys.getsizeof(tupleA)); #64 bytes

# Sets : unordered, mutable, no duplicates.

# Initialisation
setA={1,2,3};
setB=set([4,4,5,6]);
setC=set("789"); # 7,8,9
# Add element to set
setA.add(0);
setA.add((4,6))
# Pop element
setA.pop(); # return the popped element
# Remove element
setA.remove(3);
setA.discard(2);
# Clear set
setC.clear();
# Iterate through set
for i in setC:
    pass;
# Check element
if "8" in setC:
    pass;
# Union
setD=setA.union(setB);
# Inter-section
setE=setA.intersection(setD);
# Difference
setF={1,2,3,4,5};
setG={1,6,7,3};
setH=setF.difference(setG);
# Symmetric difference
setI=setF.symmetric_difference(setG);
# Intersection update
setJ=setG.intersection_update(setF);
# Difference update
setK=setG.difference_update(setF);
# Symmetric difference update
setL=setF.symmetric_difference_update(setG);
# Sub-set
setA.issubset(setB);
# Super-set
setA.issuperset(setB);
# Disjoint-set
setA.isdisjoint(setB);
print(setD);

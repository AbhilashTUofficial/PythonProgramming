# Lambda: In-line function with arguments.

# Initialisation
lambdaFuncA=lambda x:x+3;
lambdaFuncB=lambda x:x*3;
lambdaFuncC=lambda x,y:x+3*y;

a=[(1,2),(15,1),(5,-1),(10,4)];
sorted_by_x=sorted(a);
sorted_by_y=sorted(a,key=lambda x:x[1]);
sorted_by_sum=sorted(a,key=lambda x:x[0]+x[1]);
b=[1,3,5,7,9];
c=map(lambda x:x*2,b); # c=[x*2 for x in a];
d=[1,2,3,4,5,6,7];
e=filter(lambda x:x%2==0,d) # e=[x for x in a if x%2==0];
from functools import reduce
f=reduce(lambda x,y:x+y,d);

print(f)
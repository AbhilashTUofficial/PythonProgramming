# Lambda: In-line function with arguments.

# Initialisation
lambdaFuncA=lambda x:x+3;
lambdaFuncB=lambda x:x*3;
lambdaFuncC=lambda x,y:x+3*y;

a=[(1,2),(15,1),(5,-1),(10,4)];
a_sorted_by_x=sorted(a);
a_sorted_by_y=sorted(a,key=lambda x:x[1]);


print(a_sorted_by_x)
print(a_sorted_by_y)
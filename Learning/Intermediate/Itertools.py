# Itertools: Product, permutations, combinations, accumulate, groupby, and infinite iterators.

from itertools import product

# Initialisation
a=[1,2,3,4];
b=[4,5];
# product of a and b.
c=product(a,b); 
d=[6];
e=product(b,d,repeat=2);

from itertools import permutations

# Initialisation
f=permutations(b); # all possible orders.
# all the possible orders with only n elements.
g=permutations(a,2);

from itertools import combinations

# Initialisation
# all possible combintaions within length 2.
# no-repeat
h=combinations(a,2); 

from itertools import combinations_with_replacement

# repeat
i=combinations_with_replacement(a,2);

from itertools import accumulate
import operator

# Initialisation
# arr[n]=arr[n-1]+arr[n];
j=accumulate(a)
# arr[n]=arr[n-1]*arr[n];
k=accumulate(a, func=operator.mul);

from itertools import groupby

# Initialisation
def smaller_than_3(x):
    # the return will sort the input into 
    # two groups, true group and false group.
    return x<3;
# key is a function which run iteratively.
l=groupby(a,key=smaller_than_3)# key=lambda x:x<3;
for key,value in l:
    #print(key,list(value));
    pass;

m=[{'value':'one','key':1},{'value':'two','key':1},{'value':'three','key':3},{'value':'one','key':3}]
n=groupby(m,key=lambda x:x['key']);
for key,value in n:
    #print(key,list(value));
    pass;

from itertools import count

# Initialisation
for i in count(10):
    pass;

from itertools import cycle

# Initialisation
for i in cycle(a):
    pass;

from itertools import repeat

# Initialisation
for i in repeat(1,3):
    pass;

print(list(l));

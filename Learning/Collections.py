from collections import Counter
# Colletions : Couner, namedtuple, Ordered-dict, default-dict, deque.

# Counter
# Counter create dictionary with the given elements.

# Initialisation
stringA="aaabbbbcddddd";
counterA=Counter(stringA);
# CounterA
# { 'd' : 5, 'b' : 4, 'a' : 3, 'c' : 1}
# Get key-values
counterA.keys;
counterA.values;
counterA['a'];

# Pop Counter
counterA.pop('c');
counterA.popitem();
# remove key-value pair
del counterA['a'];
# Check key
if "b" in counterA:
    pass;
# iterate through counter.
for i in counterA.values(): # couterA.keys(), couterA.items(), couterA
    pass;
# Copy counter
counterB=counterA.copy();
# Dictionary from counter
dictD=dict(counterA);
# List from counter
listA=list(counterA);
# Merge dictionaries
# Update dictionaries
dictA={"one":1,"two":2};
counterA.update(dictA);
dictD.update(counterA);
# Clear Counter
#counterA.clear();
# Add elements to counter
counterA['a']=6;
counterA['z']=5;
# Get most common elements
counterA.most_common(2);
# Return a iterable with all of the values.
listB=list(counterA.elements());

from collections import namedtuple
# NamedTuple is an easy to create light weight object type, similar to a struct
# Initialisation
# This create a class 'coordinate' with fields x and y
coor=namedtuple('coordinate','x,y');
point1=coor(100,142);
# Access the values
point1;
point1.x;
point1.y;

from collections import OrderedDict
# OrderedDict are like regular dictionaries, but they will remember the order
# of item insertion. v3.7^ -> regular dictionary also remember the inserion order. 
# Initialisation
ordered_dict=OrderedDict();
ordered_dict['one']=1;
ordered_dict['two']=2;
ordered_dict['three']=3;
ordered_dict['four']=4;
ordered_dict['five']=5;

from collections import defaultdict
# The defaultdict is similar to ordinary dict, but if the it allows to give a default
# value for keys if the value is not defined.
# Initialisation
defaultdict_A=defaultdict(int);
defaultdict_A['a']=1;
defaultdict_A['b']=2;
defaultdict_A['c'];# 0

from collections import deque
# deque is an double-ended queue, just like a deque of cards.
# Initilisation
deque_A=deque();
# Adding new elements
deque_A.append(1);
deque_A.append(2);
deque_A.append(3);
deque_A.appendleft('1left');
deque_A.extend([4,5,6]);
deque_A.extendleft(['2left','3left','4left']);
# Indent list
deque_A.rotate(2);
# rotate(1) one place to the right.
# rotate(2) two place to the right.
# rotate(-1) one place to the left.
print(deque_A)
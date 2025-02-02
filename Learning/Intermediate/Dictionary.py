# Dictionary: Key-Value pairs, Unordered, Mutable

# Initialisation
dictA={
    "key1":"value1",
    "key2":"value2",
    "key3":"value3"
       };
dictB=dict(key4="value4",key5="value5",key6="value6");
dictB["key7"]="value7";
# Access key-value
dictA["key1"] # This will throw a error if key is not present.
dictA.get("keyx") # This will return none if key is not present. 
# remove key-value pair
del dictB["key4"];
# pop key-value pair
dictB.pop("key5");
dictB.popitem(); # pop the last entry
# Check key
if "key1" in dictA:
    pass;
# iterate through dictionary.
for i in dictA.values(): # dictA.keys(), dictA.items(), dictA
    pass;
# Copy dictionary
dictC=dictB.copy();
dictD=dict(dictA);
# Merge dictionaries
# Update dictionaries
dictB["key6"]="6";
dictC.update(dictD);
dictC.update(dictB);
# Clear dictionary
dictB.clear();

# create a dictionary with two arrays
import string
heights=[1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
res={}
for letter in string.ascii_lowercase:
    for h in heights:
        res[letter] = h
        h.remove(h)
        break
    
# loop through dictionary, get array of keys or values.
res2=[res[w]for w in string.ascii_lowercase]

print(dictB);

# Merge two or more dictiories.
d1={"name":"a","age":13}
d2={"name":"a","sex":"M"}

d3={**d1,**d2}

# Create dictionary form array
arr=[1,2,3]
dictE={i:arr[i]for i in range(len(arr))}

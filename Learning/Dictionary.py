# Dictionary: Key-Value pairs, Unordered, Mutable

# Initialisation
dictA={
    "key1":"value1",
    "key2":"value2",
    "key3":"value3"
       };
dictB=dict(key4="value4",key5="value5",key6="value6");
dictB["key7"]="value7";
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
print(dictB);

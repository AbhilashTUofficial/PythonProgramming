# String: Imutable, Ordered, Text representation.

# Initialisation
stringA="1234";
stringB="""
789
456
123
""";
# fist character in the String
stringA[0];
# last character in the String
stringA[-1];
# second-last character in the String
stringA[-2];
# Create a string with same sub-string multiple times.
stringJ=["z"]*3;
# Concatenage a new string
stringC=stringA+stringB;
# Split a string to chars
[l for l in stringA]
# Slice the string by interval
stringC[2:5];
# Slice the string from begining
stringC[:5];
# Slice the string to end
stringC[2:];
# Slice the string from begining to end
stringC[:];
# Slice the string by step
stringC[::2];
stringC[::1];
stringC[::-1] # Reverse the string.
# Length of the string
len(stringA);
# Convert to lower-case
stringD="AbCd";
stringD.lower();
# Convert to upper-case
stringD.upper();
# Convert to capitalized
stringD.capitalize();
# Return True or False
stringD.endswith("d");
stringD.isalnum();
stringD.islower();
stringD.isupper();
stringD.isalpha();
stringD.isascii();
stringD.isdecimal();
stringD.isdigit();
stringD.isnumeric();
stringD.isprintable();
stringD.startswith("a");
# Return index of sub-string
stringD.find("b");
# Return the count of sub-string
stringD.count("a");
# Replace sub-string with a new sub-string
stringD.replace("A","Z");
# iterate through String
for i in stringC:
    pass;
# check the sub-string in the String
if 'b' in stringD:
    pass;
# Remove white-spaces from a String
stringE="   123  ";
stringE.strip();
# Convert string to list
stringF="a b c d e";
stringG="a,b,c,d";
stringF.split();
stringG.split(",");
# Convert list to string
listA=["a","b","c"];
stringA.join(listA);
stringH=" ".join(listA);
stringI="-".join(listA);
# Formating
num=1.234
stringK="The string is %s" %stringA; # %s, %d %f %.3f
stringL="The string is {}".format(stringA);
stringL="The string is {:.3f}".format(num);
stringM="The string is {}, The number is {}".format(stringA,num)
stringK=f"The string is {stringA}, The number is {num+8}"

# array of English alphabetic letters
import string
alpha=[string.ascii_letters]
alpha=[string.ascii_lowercase]
alpha=[string.ascii_uppercase]


print(stringK)
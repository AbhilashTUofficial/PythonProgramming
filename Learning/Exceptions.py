# Raise Exception
# Build in exception, raised when certain condition is met.
# Initialisation

a=5
if a>5: raise Exception("raise error!")

# Assert Exception
# Build in exception, assert exception throw a exception when
# the given condition is not true.
# Initialisation

assert (a>=5), 'assert error!'

# try-catch Exception
# try-catch exception, used to try certain section of code catch any
# error, and throw counter meassure for it.
# Initialisation

try:
    a=1/0;
except Exception as exception:
    pass;
else:
    pass;
finally:
    pass;

# Custom build Exception
# Initialisation

class CustomError(Exception):
    def __init__(self,value):
        self.value=value;
        print("Custom Error !!!");

if(a>5): raise CustomError;






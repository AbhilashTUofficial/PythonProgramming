from log_setup import *
from error_setup import error_logger
def func0():
    logging.debug("Debug message");
    logging.info("Info message");
    logging.warning("Warning message");
    logging.error("Error message");
    logging.critical("Critical message");

def func1():
    print("Function 1");
    n=0
    try:
        print(1/n);
    except ZeroDivisionError as e:
    
        # logging.debug("n is zero \n",exc_info=True);
        error_logger.error("stream handler");
        # error_logger.warning("file handler")

func1()

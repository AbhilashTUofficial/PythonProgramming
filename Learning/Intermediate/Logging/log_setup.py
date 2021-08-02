import logging

# Basic Logging Tutorial
# Logging is a means of tracking events that happen when some software runs. 
# The software’s developer adds logging calls to their code to indicate that 
# certain events have occurred. An event is described by a descriptive message 
# which can optionally contain variable data (i.e. data that is potentially 
# different for each occurrence of the event). Events also have an importance 
# which the developer ascribes to the event; the importance can also be called 
# the level or severity.

# When to use logging
# Logging provides a set of convenience functions for simple logging usage. 
# These are debug(), info(), warning(), error() and critical(). 
# To determine when to use logging, see the table below, which states, 
# for each of a set of common tasks, the best tool to use for it.


# Task you want to perform


# print()
# Report events that occur during normal operation of a program 
# (e.g. for status monitoring or fault investigation)

# logging.info() (or logging.debug() for very detailed output for 
# diagnostic purposes)Issue a warning regarding a particular runtime event

# warnings.warn() in library code if the issue is avoidable and the client 
# application should be modified to eliminate the warning
# logging.warning() if there is nothing the client application can do about
# the situation, but the event should still be noted
# Report an error regarding a particular runtime event

# Raise an exception
# Report suppression of an error without raising an exception 
# (e.g. error handler in a long-running server process)
# logging.error(), logging.exception() or logging.critical() 
# as appropriate for the specific error and application domain

# Visit https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

# Change the logging default options.

logging.basicConfig(
    filename= 'Learning/Intermediate/Logging/log_tracker.log', 
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(filename)s - %(message)s - line : %(lineno)s',
    datefmt='%m/%d/%Y %H:%M:%S');

# default filemode : appending
# filemode = 'w : replace
# %(asctime)s  ->  time and also set datefmt to set the time.
# %filename)s  ->  get the name of the file.
# %(message)s  ->  get the message.
# %(lineno)d   ->  get the line number.
# %(funcName)s ->  get the function name.


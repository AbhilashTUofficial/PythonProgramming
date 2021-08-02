import logging
from logging import handlers

from logging.handlers import RotatingFileHandler

logger=logging.getLogger(__name__);
logger.setLevel(logging.ERROR);

handler=RotatingFileHandler('Learning/Intermediate/Logging/errorLogs/errors.log',maxBytes=2000,backupCount=0);
logger.addHandler(handler);

arr=[0]

for i in range(10):
    try:
        arr[i]=0
    except IndexError as ie:
        logger.error("Error %d: %s",i,ie,exc_info=True);
        
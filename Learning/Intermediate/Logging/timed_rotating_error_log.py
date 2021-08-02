import logging
import time
from logging import handlers

from logging.handlers import TimedRotatingFileHandler

logger=logging.getLogger(__name__);
logger.setLevel(logging.ERROR);

handler=TimedRotatingFileHandler('Learning/Intermediate/Logging/errorLogs/errors.log',when='s',interval=5,backupCount=0);
logger.addHandler(handler);

arr=[0]

for i in range(10):
    try:
        arr[i]=0
    except IndexError as ie:
        logger.error("Error %d: %s",i,ie,exc_info=True);
        time.sleep(5)
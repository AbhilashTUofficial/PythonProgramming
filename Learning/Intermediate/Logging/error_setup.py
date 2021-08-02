import logging

error_logger=logging.getLogger(__name__);
formatter=logging.Formatter('%(asctime)s - %(filename)s - %(message)s - line : %(lineno)s',datefmt='%m/%d/%Y %H:%M:%S');

stream_handler=logging.StreamHandler();
stream_handler.setLevel(logging.ERROR);
stream_handler.setFormatter(formatter);
error_logger.addHandler(stream_handler);

file_handler=logging.FileHandler('Learning/Intermediate/Logging/warning_log_tracker.log',mode='w');
file_handler.setLevel(logging.WARN);
file_handler.setFormatter(formatter);
error_logger.addHandler(file_handler);


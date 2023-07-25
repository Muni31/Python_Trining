# Create a log file such as when the content of log file exceeds the 1000 line, the new log file should get
# created and the older log file should be renamed to {logfilename}0.log , {logfilename}1.log , {logfilename}2.log etc. 

import logging
from logging.handlers import RotatingFileHandler

log_filename = 'my_log_file.log'
log_max_size = 100000  
log_max_files = 5      


rotating_handler = RotatingFileHandler(filename=log_filename, maxBytes=log_max_size, backupCount=log_max_files)
rotating_handler.setLevel(logging.DEBUG)  

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
rotating_handler.setFormatter(formatter)

logger = logging.getLogger('my_logger')
logger.addHandler(rotating_handler)

def my_function():
    logger.debug("This is a DEBUG level log message.")
    logger.info("This is an INFO level log message.")
    logger.warning("This is a WARNING level log message.")
    logger.error("This is an ERROR level log message.")
    logger.critical("This is a CRITICAL level log message.")

my_function()

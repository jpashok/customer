'''
Module which provides different type of loggers for the application
'''
from functools32 import lru_cache

from config import Config
import logging
from logging.handlers import RotatingFileHandler

@lru_cache()
def customer_logger():
    log_config = Config.get()['customer_log']
    logger = logging.getLogger('customer-api')
    logger.setLevel(log_config['level'].upper())


    #Set the rotating file handler to store 1GB of logs per file and backup count is 3 .
    #This will periodically clean up disk space and have only logs worth of 3 GB in disk
    #TODO change this when going to prod based setting
    file_handler = RotatingFileHandler(log_config['path'],maxBytes=1000000000,backupCount=3)

    formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s %(module)s : %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


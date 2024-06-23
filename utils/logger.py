import logging
from logging.handlers import RotatingFileHandler
import os

# Create a logger
logger = logging.getLogger('ChainInspectLogger')
logger.setLevel(logging.DEBUG)

# Define log file path
LOG_FILE_PATH = 'chaininspect.log'

# Create a rotating file handler
file_handler = RotatingFileHandler(filename=LOG_FILE_PATH, maxBytes=10485760, backupCount=5)
file_handler.setLevel(logging.DEBUG)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set formatter for file handler and console handler
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Example usage
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')

# Set permissions for log file
os.chmod(LOG_FILE_PATH, 0o600)

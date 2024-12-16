import logging
from datetime import datetime

# Generate log file name based on the current date
log_filename = datetime.now().strftime('visualisemoneymanager_%Y-%m-%d-%H-%M-%S.log')

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.propagate = False  # Prevent the log messages from being propagated to the root logger

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(log_filename, mode='w')

# Create formatters and add them to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
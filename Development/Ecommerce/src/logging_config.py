import logging
from logging.handlers import RotatingFileHandler
import os

# Ensure log directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
def setup_logging():
    # Root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Create handlers
    file_handler = RotatingFileHandler(os.path.join(LOG_DIR, 'app.log'), maxBytes=10485760, backupCount=3)
    product_file_handler = RotatingFileHandler(os.path.join(LOG_DIR, 'product.log'), maxBytes=10485760, backupCount=3)
    stream_handler = logging.StreamHandler()

    # Set log level for handlers
    file_handler.setLevel(logging.INFO)
    product_file_handler.setLevel(logging.INFO)
    stream_handler.setLevel(logging.INFO)

    # Create formatters and add them to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    product_file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # Add handlers to the root logger
    logger.addHandler(file_handler)
    logger.addHandler(product_file_handler)
    logger.addHandler(stream_handler)

setup_logging()

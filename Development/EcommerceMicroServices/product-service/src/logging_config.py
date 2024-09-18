import logging
import os

# Define a global logger
logger = logging.getLogger("product")

def setup_logging(service_name="product"):
    # Create a logs directory if it doesn't exist
    LOG_DIR = "logs"
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    # Log file path specific to the service
    LOG_FILE = os.path.join(LOG_DIR, f"{service_name}.log")

    # Set up logging configuration
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),  # Log to a file
            logging.StreamHandler()         # Log to the console
        ]
    )

    # Get a logger for the service
    global logger
    logger = logging.getLogger(service_name)
    return logger

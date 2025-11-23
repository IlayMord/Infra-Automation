import logging
import os

#Path to unified log file.
log_file = os.path.join(os.path.dirname(__file__), "..", "logs", "provisioning.log")

#Ensure logs directory exists.
os.makedirs(os.path.dirname(log_file), exist_ok=True)

#Create the logger.
logger = logging.getLogger("infra")
logger.setLevel(logging.INFO)

#Prevent duplicate handlers.
if not logger.handlers:
    fh = logging.FileHandler(log_file)
    fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(fh)

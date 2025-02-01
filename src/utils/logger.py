import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "chatbot.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
)

def log_error(message):
    """Salva logs de erro"""
    logging.error(message)

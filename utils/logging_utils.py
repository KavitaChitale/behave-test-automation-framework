import logging
import os
from datetime import datetime
import coloredlogs

def setup_logger(name, log_file, level=logging.DEBUG):
    logger = logging.getLogger(name)
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)
        logger.setLevel(level)
        logger.addHandler(handler)
        # Console handler
        stream_handler = logging.StreamHandler()
        stream_formatter = logging.Formatter('%(levelname)s - %(message)s')
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)
        coloredlogs.install(level=level, logger=logger, fmt='%(levelname)s - %(message)s')
    return logger

def take_screenshot(driver, scenario_name, output_dir="screenshots"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{scenario_name}_{timestamp}.png".replace(" ", "_")
    filepath = os.path.join(output_dir, filename)
    driver.save_screenshot(filepath)
    print(f"[Screenshot] Saved to: {filepath}")

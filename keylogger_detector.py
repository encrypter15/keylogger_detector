#!/usr/bin/env python3
# Keylogger Detector
# Author: Rick Hayes
# License: MIT
# Version: 2.73
# README: Requires psutil. Scans processes for potential keyloggers.

import psutil
import argparse
import logging
import json

def setup_logging():
    """Configure logging to file."""
    logging.basicConfig(filename='keylogger_detector.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_file: str) -> dict:
    """Load configuration from JSON file."""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Config loading failed: {e}")
        return {"suspicious_keywords": ["key", "log", "spy"]}

def check_process(process, keywords: list) -> bool:
    """Check if a process name contains suspicious keywords."""
    try:
        name = process.name().lower()
        return any(keyword in name for keyword in keywords)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return False

def main():
    """Main function to parse args and detect keyloggers."""
    parser = argparse.ArgumentParser(description="Keylogger Detector")
    parser.add_argument("--config", default="config.json", help="Config file path")
    args = parser.parse_args()

    setup_logging()
    config = load_config(args.config)

    logging.info("Scanning processes for potential keyloggers")
    for proc in psutil.process_iter(['pid', 'name']):
        if check_process(proc, config["suspicious_keywords"]):
            info = f"Suspicious process: PID {proc.pid}, Name: {proc.name()}"
            logging.warning(info)
            print(info)

    logging.info("Scan completed")
    print("Scan completed")

if __name__ == "__main__":
    main()

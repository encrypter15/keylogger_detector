# Keylogger Detector

## Overview
The Keylogger Detector is a Python tool that scans running processes for potential keyloggers using the `psutil` library. It flags processes based on suspicious keywords in their names.

## Author
Rick Hayes

## License
MIT

## Version
2.73

## Requirements
- Python 3.x
- `psutil` library (`pip install psutil`)
- Sufficient permissions to access process information

## Usage
Run the script with the following argument:

```bash
python3 keylogger_detector.py [--config <CONFIG_FILE>]

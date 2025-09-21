# Regex-Based Log Analyzer

## Overview
A Python tool to ingest server or application logs and extract insights (e.g., errors, slow endpoints) using regex filters. Supports both CLI and GUI.

## Features
- Accepts log files and regex patterns
- Displays summary statistics (error/warning counts, top endpoints, top IPs)
- Handles malformed lines gracefully
- CLI and GUI interfaces
- Export results from GUI

## Step-by-Step Usage

### 1. Install Dependencies
```bash
pip install pytest
```

### 2. Prepare Your Log File
Place your log file (e.g., `sample.log`) in the project directory.

### 3. Run the CLI
```bash
python src/cli.py sample.log "Error|Warning"
```
- Replace `"Error|Warning"` with any regex pattern you want to filter log lines.

### 4. Run the GUI
```bash
python src/gui.py
```
- Select your log file.
- Enter a regex pattern.
- Choose Top N (3, 5, or 10).
- Click **Analyze** to view results.
- Click **Export Results** to save output.

### 5. Run Tests
```bash
pytest
```
- This will run all tests in the `tests` folder to verify core logic.

## Example Pytest Tests

See `tests/test_core.py` and `tests/test_log_analyzer.py` for core logic tests.

## Requirements
- Python 3.13+
- pytest

## Authors
Group 11

## License
MIT
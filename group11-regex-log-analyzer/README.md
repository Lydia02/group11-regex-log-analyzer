
# Regex-Based Log Analyzer

## Overview
A Python tool to ingest server or application logs and extract insights (e.g., errors, slow endpoints) using regex filters. Supports both CLI and GUI.

## Features
- Accepts log files and regex patterns
- Displays summary statistics (error/warning counts, top endpoints, top IPs)
- Handles malformed lines gracefully
- CLI and GUI interfaces
- Export results from GUI

## Usage

### CLI
```bash
python src/cli.py sample.log "Error|Warning"
```

### GUI
```bash
python src/gui.py
```
Select your log file, enter a regex pattern, choose Top N, and click Analyze.

## Testing

Run all tests:
```bash
pytest
```

## Example Pytest Tests

See `tests/test_core_logic.py` for core logic tests.

## Requirements
- Python 3.13+
- pytest

## Authors
Group 11

## License
MIT
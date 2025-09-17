# Group 11 Regex-Based Log Analyzer

## Purpose
Analyze log files using regex to extract errors, warnings, and top endpoints.

## Usage
```bash
pipenv run python src/cli.py <logfile> <pattern> [--endpoint-pattern <regex>]
```

## Features
- Parse log files
- Apply regex patterns
- Count errors/warnings
- Show top endpoints
- Handles invalid regex gracefully

## Team Roles
- Coordinator/Lead
- Developer
- QA/CI & Tests
- Docs/Presenter
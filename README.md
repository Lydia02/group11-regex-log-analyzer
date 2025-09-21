
A Python-based log analysis tool with both CLI and Tkinter GUI.
It allows users to ingest server/application logs, filter entries using regex, and extract insights such as error/warning counts, top endpoints, and top IP addresses.

---

## Setup Instructions

### 1. Install Python
This project requires Python 3.13.

If you already have Python 3.13, you’re good to go.
If you have Python 3.12 or earlier, install Python 3.13 from [python.org](https://www.python.org/downloads/).

**Verify your Python version:**
```bash
python --version
```

### 2. Clone the repository
```bash
git clone https://github.com/Lydia02/group11-regex-log-analyzer.git
cd group11-regex-log-analyzer/group11-regex-log-analyzer
```

### 3. Install Pipenv (if not already installed)
```bash
pip install pipenv
```

### 4. Install dependencies
```bash
pipenv install --dev
```

### 5. Activate the virtual environment
```bash
pipenv shell
```

---

## Running the Application

### Run the CLI
```bash
python src/cli.py sample.log "Error|Warning"
```
- Replace `"Error|Warning"` with any regex pattern you want to filter log lines.

### Run the GUI
```bash
python src/gui.py
```
- Select your log file.
- Enter a regex pattern.
- Choose Top N (3, 5, or 10).
- Click **Analyze** to view results.
- Click **Export Results** to save output.

---

## Running Tests

Tests are located in the `tests/` folder.

Run all tests:
```bash
pytest
```
Or:
```bash
pipenv run pytest
```
Run a specific test file:
```bash
pytest tests/test_core.py
```


---

## Project Structure

```
group11-regex-log-analyzer/
│── src/
│    ├── cli.py               # CLI entry point
│    ├── gui.py               # Tkinter GUI entry point
│    ├── log_analyzer.py      # Core log analysis logic
│    ├── log_entry.py         # Log entry parsing logic
│    └── __init__.py
│── tests/
│    ├── test_core.py         # Core logic tests
│    ├── test_log_analyzer.py # LogAnalyzer tests
│    └── __pycache__/
│── sample.log                # Example log file
│── Pipfile                   # Dependency management
│── README.md                 # Project documentation
```
---

## Roles & Contributions

- Lydia02 [Team Lead, Docs, Presenter] – Coordination, documentation, demo video, codebase integration
- [Other team members] – Core logic, GUI, CLI, regex filtering, testing

The commit history in this repository reflects each member’s contributions in line with the roles above.

---

## Demo Video

[Video Link](https://drive.google.com/file/d/1TrGF6V11kVkxg1gSw6mR4GmM5a0_0y6H/view?usp=sharing)

---

## <img width="1303" height="739" alt="image" src="https://github.com/user-attachments/assets/698bd403-f3b0-4c31-b7e5-3101889a5c9d" />


1. **GUI Main Window**
   - Select log file, enter regex, choose Top N, analyze and export results.

2. **CLI Output**
   - Shows error/warning counts, top endpoints, and top IP addresses.

---

## License

MIT

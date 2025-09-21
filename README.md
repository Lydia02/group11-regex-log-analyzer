# Regex-Based Log Analyzer (Group 11)

A Python-based log analysis tool with both CLI and Tkinter GUI.  
It allows users to ingest server/application logs, filter entries using regex, and extract insights such as error/warning counts, top endpoints, and top IP addresses.

---

## 🚀 Quick Start

### 1. Install Python
- This project requires **Python 3.13**.
- Download from [python.org](https://www.python.org/downloads/) if needed.

**Check your Python version:**
```bash
python --version
```

### 2. Clone the Repository
Open your terminal and run:
```bash
git clone https://github.com/Lydia02/group11-regex-log-analyzer.git
cd group11-regex-log-analyzer
```

### 3. Install Pipenv (if not already installed)
```bash
pip install pipenv
```

### 4. Install Dependencies
```bash
pipenv install --dev
```

### 5. Activate the Virtual Environment
```bash
pipenv shell
```

---

## 🖥️ How to Run

### Run the CLI
From the project root, run:
```bash
python src/cli.py ../sample.log "Error|Warning"
```
- `sample.log` is your log file (provided in the project root).
- `"Error|Warning"` is a sample regex pattern. You can use any regex pattern you want.

**Common patterns:**
- `"Error"` — Only error lines
- `"Warning"` — Only warning lines
- `"GET"` — Only GET requests

### Run the GUI
From the project root, run:
```bash
python group11/src/gui.py
```
**In the GUI:**
- Click **Browse** to select your log file (e.g., `sample.log`).
- Enter a regex pattern.
- Choose Top N (3, 5, or 10).
- Click **Analyze** to view results.
- Click **Export Results** to save output.

---

## 🧪 Running Tests

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

## 📂 Project Structure

```
group11-regex-log-analyzer/
│── group11/
│    └── src/
│         ├── cli.py               # CLI entry point
│         ├── gui.py               # Tkinter GUI entry point
│         ├── log_analyzer.py      # Core log analysis logic
│         ├── log_entry.py         # Log entry parsing logic
│         └── __init__.py
│── tests/
│    ├── test_core.py         # Core logic tests
│    ├── test_log_analyzer.py # LogAnalyzer tests
│    └── __pycache__/
│── sample.log                # Example log file
│── Pipfile                   # Dependency management
│── README.md                 # Project documentation
```

---

## 👥 Roles & Contributions

- **Lydia02** [Team Lead, Docs, Presenter] – Coordination, documentation, demo video, codebase integration
- **Other team members** – Core logic, GUI, CLI, regex filtering, testing

The commit history in this repository reflects each member’s contributions in line with the roles above.

---

## 🎥 Demo Video

[Watch the Demo](https://drive.google.com/file/d/1TrGF6V11kVkxg1gSw6mR4GmM5a0_0y6H/view?usp=sharing)

---

<img width="947" height="268" alt="image" src="https://github.com/user-attachments/assets/de30ff1c-4441-4fe3-8bb0-7228642739b7" />

1. **GUI Main Window**
   - Select log file, enter regex, choose Top N, analyze and export results.

2. **CLI Output**
   - Shows error/warning counts, top endpoints, and top IP addresses.

---

## ❓ Troubleshooting

- **FileNotFoundError:**  
  Make sure you run the CLI from the project root and use the correct path to your log file.
  Example:
  ```bash
  python group11/src/cli.py sample.log "Error|Warning"
  ```
- **No output or unexpected results:**  
  Check your regex pattern and ensure your log file contains matching lines.

---

## 📄 License

MIT

---

**Need help?**  
Open an issue on GitHub or contact the team lead.

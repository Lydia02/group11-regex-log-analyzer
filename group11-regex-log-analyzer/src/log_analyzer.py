import re
from collections import Counter
from log_entry import LogEntry

class LogAnalyzer:
    def __init__(self, filepath):
        self.entries = []
        self.load_log_file(filepath)

    def load_log_file(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        entry = LogEntry(line.strip())
                        self.entries.append(entry)
                    except Exception as e:
                        print(f"Malformed line skipped: {line.strip()} ({e})")
        except FileNotFoundError:
            print(f"File not found: {filepath}")

    def count_errors_warnings(self):
        errors = sum(1 for entry in self.entries if entry.error)
        warnings = sum(1 for entry in self.entries if entry.warning)
        return errors, warnings

    def top_endpoints(self, top_n=5):
        endpoints = [entry.endpoint for entry in self.entries if entry.endpoint]
        return Counter(endpoints).most_common(top_n)

    def top_ips(self, top_n=5):
        ips = [entry.ip_address for entry in self.entries if entry.ip_address]
        return Counter(ips).most_common(top_n)

    def apply_regex(self, pattern):
        try:
            regex = re.compile(pattern)
        except re.error as e:
            raise ValueError(f"Invalid regex: {e}")
        return [entry for entry in self.entries if regex.search(entry.raw_line)]
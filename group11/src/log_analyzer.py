import re
from collections import Counter
from log_entry import LogEntry


class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.entries = []
        self.load_log()

    def load_log(self):
        """Load and parse log entries from file"""
        try:
            with open(self.log_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:  # Skip empty lines
                        try:
                            entry = LogEntry(line)
                            self.entries.append(entry)
                        except Exception:
                            # Skip malformed lines
                            continue
        except FileNotFoundError:
            raise FileNotFoundError(f"Log file not found: {self.log_file}")

    def apply_regex(self, pattern):
        """Filter log entries based on regex pattern"""
        try:
            regex = re.compile(pattern, re.IGNORECASE)
        except re.error as e:
            raise ValueError(f"Invalid regex pattern: {e}")

        filtered_entries = []
        for entry in self.entries:
            if regex.search(entry.raw_line):
                filtered_entries.append(entry)

        return filtered_entries

    def count_errors_warnings(self):
        """Count errors and warnings in loaded entries"""
        errors = sum(1 for entry in self.entries if entry.error)
        warnings = sum(1 for entry in self.entries if entry.warning)
        return errors, warnings

    def top_endpoints(self, n=5):
        """Get top N endpoints by frequency"""
        endpoints = [entry.endpoint for entry in self.entries if entry.endpoint]
        counter = Counter(endpoints)
        return counter.most_common(n)

    def top_ips(self, n=5):
        """Get top N IP addresses by frequency"""
        ips = [entry.ip_address for entry in self.entries if entry.ip_address]
        counter = Counter(ips)
        return counter.most_common(n)

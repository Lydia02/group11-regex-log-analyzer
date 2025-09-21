import re

class LogEntry:
    def __init__(self, raw_line):
        self.raw_line = raw_line
        self.error = "error" in raw_line.lower()
        self.warning = "warning" in raw_line.lower()
        self.endpoint = self.extract_endpoint()
        self.ip_address = self.extract_ip()

    def extract_endpoint(self):
        match = re.search(r"GET (\S+)", self.raw_line)
        return match.group(1) if match else None

    def extract_ip(self):
        match = re.search(r"(\d{1,3}(?:\.\d{1,3}){3})", self.raw_line)
        return match.group(1) if match else None

    def is_error(self):
        return self.error

    def is_warning(self):
        return self.warning

    def __str__(self):
        return (
            f"Raw: {self.raw_line}\n"
            f"Error: {self.error}, Warning: {self.warning}\n"
            f"Endpoint: {self.endpoint}, IP: {self.ip_address}\n"
        )

    def export(self):
        return {
            "raw_line": self.raw_line,
            "error": self.error,
            "warning": self.warning,
            "endpoint": self.endpoint,
            "ip_address": self.ip_address,
        }
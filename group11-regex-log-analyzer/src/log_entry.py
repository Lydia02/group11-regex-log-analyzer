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

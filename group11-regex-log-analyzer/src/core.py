import re
from collections import Counter

def load_log_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.readlines()

def apply_regex(lines, pattern):
    try:
        regex = re.compile(pattern)
    except re.error as e:
        raise ValueError(f"Invalid regex: {e}")
    return [line for line in lines if regex.search(line)]

def count_errors_warnings(lines):
    error_count = sum(1 for line in lines if 'error' in line.lower())
    warning_count = sum(1 for line in lines if 'warning' in line.lower())
    return error_count, warning_count

def top_endpoints(lines, endpoint_pattern, top_n=5):
    regex = re.compile(endpoint_pattern)
    endpoints = [regex.search(line).group(1) for line in lines if regex.search(line)]
    return Counter(endpoints).most_common(top_n)
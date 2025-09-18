import sys
import os
import pytest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from log_entry import LogEntry
from log_analyzer import LogAnalyzer


def test_apply_regex():
    lines = ["Error: something broke", "Warning: disk almost full", "Info: all good"]
    # Simulate LogEntry objects
    entries = [LogEntry(line) for line in lines]
    analyzer = LogAnalyzer.__new__(LogAnalyzer)
    analyzer.entries = entries
    filtered = analyzer.apply_regex(r"Error|Warning")
    assert len(filtered) == 2


def test_count_errors_warnings():
    lines = ["Error: fail", "Warning: disk", "Info: ok", "error: again"]
    entries = [LogEntry(line) for line in lines]
    analyzer = LogAnalyzer.__new__(LogAnalyzer)
    analyzer.entries = entries
    errors, warnings = analyzer.count_errors_warnings()
    assert errors == 2
    assert warnings == 1

import sys
import os
import pytest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from log_entry import LogEntry
from log_analyzer import LogAnalyzer


def test_log_entry_extraction():
    line = "192.168.1.1 GET /api/data Error: Something went wrong"
    entry = LogEntry(line)
    assert entry.error is True
    assert entry.warning is False
    assert entry.endpoint == "/api/data"
    assert entry.ip_address == "192.168.1.1"


def test_log_analyzer_counts(tmp_path):
    log_content = [
        "192.168.1.1 GET /api/data Error: Something went wrong",
        "10.0.0.2 GET /api/user Warning: Disk space low",
        "127.0.0.1 GET /api/data Info: All good",
        "10.0.0.2 GET /api/user Error: Timeout",
    ]
    log_file = tmp_path / "test.log"
    log_file.write_text("\n".join(log_content))

    analyzer = LogAnalyzer(str(log_file))
    errors, warnings = analyzer.count_errors_warnings()
    assert errors == 2
    assert warnings == 1


def test_top_endpoints_and_ips(tmp_path):
    log_content = [
        "192.168.1.1 GET /api/data Error: Something went wrong",
        "10.0.0.2 GET /api/user Warning: Disk space low",
        "127.0.0.1 GET /api/data Info: All good",
        "10.0.0.2 GET /api/user Error: Timeout",
    ]
    log_file = tmp_path / "test.log"
    log_file.write_text("\n".join(log_content))

    analyzer = LogAnalyzer(str(log_file))
    top_eps = analyzer.top_endpoints()
    top_ips = analyzer.top_ips()
    assert top_eps[0][0] == "/api/data"
    assert top_eps[0][1] == 2
    assert top_ips[0][0] == "10.0.0.2"
    assert top_ips[0][1] == 2

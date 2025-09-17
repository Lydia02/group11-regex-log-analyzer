import argparse
from log_analyzer import LogAnalyzer

def main():
    parser = argparse.ArgumentParser(description="Regex-Based Log Analyzer")
    parser.add_argument("logfile", help="Path to the log file")
    parser.add_argument("pattern", help="Regex pattern to filter log lines")
    parser.add_argument("--endpoint-pattern", default=r'GET (\S+)', help="Regex to extract endpoints (default: GET <endpoint>)")
    args = parser.parse_args()

    analyzer = LogAnalyzer(args.logfile)
    try:
        filtered_entries = analyzer.apply_regex(args.pattern)
        errors, warnings = analyzer.count_errors_warnings()
        print(f"Errors: {errors}, Warnings: {warnings}")

        top_eps = analyzer.top_endpoints()
        print("Top Endpoints:")
        for ep, count in top_eps:
            print(f"{ep}: {count}")

        top_ips = analyzer.top_ips()
        print("Top IP Addresses:")
        for ip, count in top_ips:
            print(f"{ip}: {count}")
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
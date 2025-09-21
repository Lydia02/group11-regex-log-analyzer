import argparse
from log_analyzer import LogAnalyzer

class LogAnalyzerCLI:
    def __init__(self, logfile, pattern, endpoint_pattern):
        self.analyzer = LogAnalyzer(logfile)
        self.pattern = pattern
        self.endpoint_pattern = endpoint_pattern

    def run(self):
        try:
            filtered_entries = self.analyzer.apply_regex(self.pattern)
            temp_analyzer = LogAnalyzer.__new__(LogAnalyzer)
            temp_analyzer.entries = filtered_entries

            errors, warnings = temp_analyzer.count_errors_warnings()
            print(f"Errors: {errors}, Warnings: {warnings}")

            top_eps = temp_analyzer.top_endpoints()
            print("Top Endpoints:")
            for ep, count in top_eps:
                print(f"{ep}: {count}")

            top_ips = temp_analyzer.top_ips()
            print("Top IP Addresses:")
            for ip, count in top_ips:
                print(f"{ip}: {count}")

        except ValueError as ve:
            print(ve)

def main():
    parser = argparse.ArgumentParser(description="Regex-Based Log Analyzer")
    parser.add_argument("logfile", help="Path to the log file")
    parser.add_argument("pattern", help="Regex pattern to filter log lines")
    parser.add_argument(
        "--endpoint-pattern",
        default=r"GET (\S+)",
        help="Regex to extract endpoints (default: GET <endpoint>)",
    )
    args = parser.parse_args()

    cli = LogAnalyzerCLI(args.logfile, args.pattern, args.endpoint_pattern)
    cli.run()

if __name__ == "__main__":
    main()
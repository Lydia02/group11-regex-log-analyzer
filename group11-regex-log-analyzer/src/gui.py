import tkinter as tk
from tkinter import filedialog, messagebox
from log_analyzer import LogAnalyzer

class LogAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Regex Log Analyzer")

        self.log_file_var = tk.StringVar()
        self.pattern_var = tk.StringVar()
        self.top_n_var = tk.StringVar(value="5")

        tk.Label(root, text="Log File:").grid(row=0, column=0, sticky="e")
        tk.Entry(root, textvariable=self.log_file_var, width=40).grid(row=0, column=1)
        tk.Button(root, text="Browse", command=self.open_file).grid(row=0, column=2)

        tk.Label(root, text="Regex Pattern:").grid(row=1, column=0, sticky="e")
        tk.Entry(root, textvariable=self.pattern_var, width=40).grid(row=1, column=1, columnspan=2)

        tk.Label(root, text="Top N:").grid(row=2, column=0, sticky="e")
        tk.OptionMenu(root, self.top_n_var, "3", "5", "10").grid(row=2, column=1, sticky="w")

        tk.Button(root, text="Analyze", command=self.run_analysis).grid(row=2, column=2, pady=10)
        tk.Button(root, text="Export Results", command=self.export_results).grid(row=3, column=2, pady=10)

        self.result_text = tk.Text(root, width=60, height=20)
        self.result_text.grid(row=4, column=0, columnspan=3)

    def analyze_log(self, filepath, pattern, top_n):
        analyzer = LogAnalyzer(filepath)
        try:
            filtered_entries = analyzer.apply_regex(pattern)
            temp_analyzer = LogAnalyzer.__new__(LogAnalyzer)
            temp_analyzer.entries = filtered_entries

            errors, warnings = temp_analyzer.count_errors_warnings()
            top_eps = temp_analyzer.top_endpoints(int(top_n))
            top_ips = temp_analyzer.top_ips(int(top_n))

            result = f"Errors: {errors}, Warnings: {warnings}\n\nTop Endpoints:\n"
            for ep, count in top_eps:
                result += f"{ep}: {count}\n"
            result += "\nTop IP Addresses:\n"
            for ip, count in top_ips:
                result += f"{ip}: {count}\n"
            return result
        except Exception as e:
            return str(e)

    def open_file(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            self.log_file_var.set(filepath)

    def run_analysis(self):
        filepath = self.log_file_var.get()
        pattern = self.pattern_var.get()
        top_n = self.top_n_var.get()
        if not filepath or not pattern:
            messagebox.showerror("Error", "Please select a log file and enter a regex pattern.")
            return
        result = self.analyze_log(filepath, pattern, top_n)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def export_results(self):
        result = self.result_text.get(1.0, tk.END)
        filepath = filedialog.asksaveasfilename(defaultextension=".txt")
        if filepath:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(result)
            messagebox.showinfo("Export", "Results exported successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = LogAnalyzerGUI(root)
    root.mainloop()
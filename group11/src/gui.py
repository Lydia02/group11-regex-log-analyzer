import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from log_analyzer import LogAnalyzer

class LogAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Regex Log Analyzer")
        self.root.configure(bg="#f7f7f7")
        self.root.minsize(900, 500)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Main frame for padding and structure
        main_frame = tk.Frame(root, bg="#f7f7f7", padx=20, pady=20)
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.grid_rowconfigure(4, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Log file selection
        tk.Label(main_frame, text="Log File:", bg="#f7f7f7", font=("Arial", 11)).grid(row=0, column=0, sticky="e")
        self.log_file_var = tk.StringVar()
        tk.Entry(main_frame, textvariable=self.log_file_var, width=40, font=("Arial", 11)).grid(row=0, column=1, padx=5, sticky="ew")
        tk.Button(main_frame, text="Browse", command=self.open_file, font=("Arial", 10)).grid(row=0, column=2, padx=5)

        # Regex pattern
        tk.Label(main_frame, text="Regex Pattern:", bg="#f7f7f7", font=("Arial", 11)).grid(row=1, column=0, sticky="e")
        self.pattern_var = tk.StringVar()
        tk.Entry(main_frame, textvariable=self.pattern_var, width=40, font=("Arial", 11)).grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

        # Top N selection
        tk.Label(main_frame, text="Top N:", bg="#f7f7f7", font=("Arial", 11)).grid(row=2, column=0, sticky="e")
        self.top_n_var = tk.StringVar(value="5")
        tk.OptionMenu(main_frame, self.top_n_var, "3", "5", "10").grid(row=2, column=1, sticky="w", padx=5)

        # Analyze and Export buttons
        tk.Button(main_frame, text="Analyze", command=self.run_analysis, font=("Arial", 10), bg="#e6f2ff").grid(row=2, column=2, pady=10, padx=5)
        tk.Button(main_frame, text="Export Results", command=self.export_results, font=("Arial", 10), bg="#e6ffe6").grid(row=3, column=2, pady=10, padx=5)

        # Results text area
        self.result_text = tk.Text(main_frame, width=70, height=20, font=("Consolas", 10), bg="#ffffff", bd=2, relief="groove")
        self.result_text.grid(row=4, column=0, columnspan=3, pady=10, sticky="nsew")

        # Error card frame (hidden by default)
        self.error_card = tk.Frame(main_frame, bg="#ffe6e6", bd=2, relief="groove")
        self.error_label = tk.Label(self.error_card, text="", bg="#ffe6e6", fg="#b30000", font=("Arial", 11, "bold"), wraplength=400, justify="center")
        self.error_label.pack(padx=10, pady=10)
        self.ok_button = tk.Button(self.error_card, text="OK", command=self.hide_error_card, font=("Arial", 10), bg="#ffcccc")
        self.ok_button.pack(pady=(0,10))
        self.error_card.grid(row=5, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
        self.error_card.grid_remove()

    def show_error_card(self, message):
        self.error_label.config(text=message)
        self.error_card.grid()
        self.error_card.lift()

    def hide_error_card(self):
        self.error_card.grid_remove()

    def analyze_log(self, filepath, pattern, top_n):
        try:
            analyzer = LogAnalyzer(filepath)
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
            self.show_error_card(str(e))
            return ""

    def open_file(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            self.log_file_var.set(filepath)
            # Check if file is valid
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    f.readline()
            except Exception as e:
                self.show_error_card(f"Error opening file: {e}")

    def run_analysis(self):
        filepath = self.log_file_var.get()
        pattern = self.pattern_var.get()
        top_n = self.top_n_var.get()
        if not filepath or not pattern:
            self.show_error_card("Please select a log file and enter a regex pattern.")
            return
        result = self.analyze_log(filepath, pattern, top_n)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def export_results(self):
        result = self.result_text.get(1.0, tk.END)
        filepath = filedialog.asksaveasfilename(defaultextension=".txt")
        if filepath:
            try:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(result)
                messagebox.showinfo("Export", "Results exported successfully!")
            except Exception as e:
                self.show_error_card(f"Export failed: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LogAnalyzerGUI(root)
    root.mainloop()
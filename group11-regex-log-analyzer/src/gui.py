import tkinter as tk
from tkinter import filedialog, messagebox
from log_analyzer import LogAnalyzer

def analyze_log(filepath, pattern, top_n):
    analyzer = LogAnalyzer(filepath)
    try:
        analyzer.apply_regex(pattern)
        errors, warnings = analyzer.count_errors_warnings()
        top_eps = analyzer.top_endpoints(top_n)
        top_ips = analyzer.top_ips(top_n)
        result = f"Errors: {errors}, Warnings: {warnings}\n\nTop Endpoints:\n"
        for ep, count in top_eps:
            result += f"{ep}: {count}\n"
        result += "\nTop IP Addresses:\n"
        for ip, count in top_ips:
            result += f"{ip}: {count}\n"
        return result
    except Exception as e:
        return str(e)

def open_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        log_file_var.set(filepath)

def run_analysis():
    filepath = log_file_var.get()
    pattern = pattern_var.get()
    top_n = int(top_n_var.get())
    if not filepath or not pattern:
        messagebox.showerror("Error", "Please select a log file and enter a regex pattern.")
        return
    result = analyze_log(filepath, pattern, top_n)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

def export_results():
    result = result_text.get(1.0, tk.END)
    filepath = filedialog.asksaveasfilename(defaultextension=".txt")
    if filepath:
        with open(filepath, "w", encoding='utf-8') as f:
            f.write(result)
        messagebox.showinfo("Export", "Results exported successfully!")

root = tk.Tk()
root.title("Regex Log Analyzer")

log_file_var = tk.StringVar()
pattern_var = tk.StringVar()
top_n_var = tk.StringVar(value="5")

tk.Label(root, text="Log File:").grid(row=0, column=0, sticky="e")
tk.Entry(root, textvariable=log_file_var, width=40).grid(row=0, column=1)
tk.Button(root, text="Browse", command=open_file).grid(row=0, column=2)

tk.Label(root, text="Regex Pattern:").grid(row=1, column=0, sticky="e")
tk.Entry(root, textvariable=pattern_var, width=40).grid(row=1, column=1, columnspan=2)

tk.Label(root, text="Top N:").grid(row=2, column=0, sticky="e")
tk.OptionMenu(root, top_n_var, "3", "5", "10").grid(row=2, column=1, sticky="w")

tk.Button(root, text="Analyze", command=run_analysis).grid(row=2, column=2, pady=10)
tk.Button(root, text="Export Results", command=export_results).grid(row=3, column=2, pady=10)

result_text = tk.Text(root, width=60, height=20)
result_text.grid(row=4, column=0, columnspan=3)

root.mainloop()
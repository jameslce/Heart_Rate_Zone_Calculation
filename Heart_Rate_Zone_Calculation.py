# -------------------------------
# Heart Rate Zone Calculation Methods
# -------------------------------

# 1. %MHR Method (Percentage of Maximum Heart Rate)
# Formula:
#   Target HR = MHR × Intensity
# Where:
#   MHR = Maximum Heart Rate (commonly estimated as 220 - age)
# Example:
#   For MHR = 196 and Zone 1 (50–60%):
#     Target HR = 196 × 0.50 to 196 × 0.60 → 98–117 bpm
#
# Pros: Simple and commonly used
# Cons: Doesn't account for individual resting heart rate

# 2. Karvonen Method (Heart Rate Reserve Method)
# Formula:
#   HRR = MHR - RHR
#   Target HR = RHR + (HRR × Intensity)
# Where:
#   RHR = Resting Heart Rate
# Example:
#   For MHR = 196, RHR = 55, HRR = 141, Zone 1 (50–60%):
#     Target HR = 55 + (141 × 0.50 to 0.60) → 125–139 bpm
#
# Pros: More personalized, considers resting heart rate
# Cons: Slightly more complex to compute

# 3. MAF Method (Maximum Aerobic Function by Dr. Phil Maffetone)
# Formula:
#   MAF HR = 180 − Age + Adjustment
# Adjustment guidelines:
#   +5 → Experienced athlete, consistent training
#    0 → Average individual with regular training
#   -5 → Beginner, recent injury, or recovering
# Example:
#   For Age = 45, no adjustment:
#     MAF HR = 180 − 45 = 135 bpm (typically Zone 2 base)
#
# Pros: Focused on building aerobic base, good for endurance
# Cons: Not a full zone model, less applicable for higher intensities

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

def calculate_zones():
    try:
        birth_year = int(entry_birth_year.get())
        mhr = int(entry_mhr.get())
        rhr = int(entry_rhr.get())

        current_year = datetime.now().year
        if not (1900 <= birth_year <= current_year):
            raise ValueError("Invalid birth year.")
        if not (100 <= mhr <= 220):
            raise ValueError("Invalid Max HR. Should be between 100–220.")
        if not (30 <= rhr <= 100):
            raise ValueError("Invalid Resting HR. Should be between 30–100.")
        if rhr >= mhr:
            raise ValueError("Resting HR must be less than Max HR.")

        age = current_year - birth_year
        hrr = mhr - rhr

        zones_mhr = [(0.50, 0.60), (0.60, 0.70), (0.70, 0.80), (0.80, 0.90), (0.90, 1.00)]
        zones_karvonen = [(0.50, 0.60), (0.60, 0.70), (0.70, 0.80), (0.80, 0.90), (0.90, 1.00)]

        for row in tree.get_children():
            tree.delete(row)

        for i, (z_mhr, z_karv) in enumerate(zip(zones_mhr, zones_karvonen)):
            zone = f"Zone {i+1}"
            mhr_range = f"{int(mhr * z_mhr[0])}–{int(mhr * z_mhr[1])}"
            karv_range = f"{int(rhr + hrr * z_karv[0])}–{int(rhr + hrr * z_karv[1])}"
            maf_base = 180 - age
            maf_range = (
                f"< {maf_base}" if i == 0 else
                f"{maf_base}–{maf_base + 5}" if i == 1 else
                f"> {maf_base + 5}" if i == 2 else
                "N/A"
            )
            tree.insert("", "end", values=(zone, mhr_range, karv_range, maf_range))

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))


# Setup GUI
root = tk.Tk()
root.title("Heart Rate Zone Calculator")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# Remove maximize/minimize buttons (Windows only)
root.attributes('-toolwindow', True)

style = ttk.Style()
style.theme_use("default")

style.configure("Treeview", 
                background="#2e2e2e",
                foreground="white",
                rowheight=25,
                fieldbackground="#2e2e2e",
                bordercolor="#444",
                borderwidth=1)
style.map('Treeview', background=[('selected', '#4a6984')])

style.configure("Treeview.Heading", 
                background="#1e1e1e",
                foreground="white",
                relief="flat")

# Input Frame
frame_input = tk.Frame(root, bg="#1e1e1e")
frame_input.grid(row=0, column=0, padx=10, pady=10, sticky="w")

tk.Label(frame_input, text="Year of Birth:", fg="white", bg="#1e1e1e").grid(row=0, column=0, sticky="e")
entry_birth_year = tk.Entry(frame_input)
entry_birth_year.grid(row=0, column=1, padx=5)

tk.Label(frame_input, text="Max HR (MHR):", fg="white", bg="#1e1e1e").grid(row=1, column=0, sticky="e")
entry_mhr = tk.Entry(frame_input)
entry_mhr.grid(row=1, column=1, padx=5)

tk.Label(frame_input, text="Resting HR (RHR):", fg="white", bg="#1e1e1e").grid(row=2, column=0, sticky="e")
entry_rhr = tk.Entry(frame_input)
entry_rhr.grid(row=2, column=1, padx=5)

tk.Button(frame_input, text="Calculate Zones", command=calculate_zones).grid(row=3, column=0, columnspan=2, pady=10)

# Output Table
columns = ("Zone", "%MHR (bpm)", "Karvonen (bpm)", "MAF (bpm)")
tree = ttk.Treeview(root, columns=columns, show="headings", height=7)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=140)

tree.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()

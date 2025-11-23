import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        
        w = weight_entry.get()
        h = height_entry.get()
        
        if not w or not h:
            messagebox.showwarning("Missing Info", "Please enter both weight and height.")
            return

        weight = float(w)
        height = float(h)

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Values must be positive.")
            return

        bmi = weight / (height ** 2)
        
        category = ""
        color = "black"
        
        if bmi < 18.5:
            category = "Underweight ⚠️"
            color = "#3498bb"
        elif 18.5 <= bmi < 25:
            category = "Healthy Weight ✨"
            color = "#2ecb71"
        elif 25 <= bmi < 30:
            category = "Overweight 🍩"
            color = "#f39c12"
        else:
            category = "Obesity 🍰⚠️"
            color = "#e74c3c"

        # Update labels
        result_lbl.config(text=f"BMI: {bmi:.2f}", fg="#2c3e50")
        status_lbl.config(text=f"{category}", fg=color)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x320")
root.config(bg="#ecf0f1")
root.resizable(False, False)


frame = tk.Frame(root, bg="#ecf0f1")
frame.pack(pady=30)


tk.Label(frame, text="Weight (kg):", bg="#ecf0f1", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
weight_entry = tk.Entry(frame, font=("Arial", 11), width=10)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame, text="Height (m):", bg="#ecf0f1", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
height_entry = tk.Entry(frame, font=("Arial", 11), width=10)
height_entry.grid(row=1, column=1, padx=10, pady=10)


calc_btn = tk.Button(frame, text="Calculate", command=calculate, font=("Arial", 10, "bold"), bg="white", relief="groove")
calc_btn.grid(row=2, columnspan=2, pady=20, sticky="we")


result_lbl = tk.Label(root, text="", bg="#ecf0f1", font=("Helvetica", 16, "bold"))
result_lbl.pack()

status_lbl = tk.Label(root, text="", bg="#ecf0f1", font=("Helvetica", 14))
status_lbl.pack()

root.mainloop()
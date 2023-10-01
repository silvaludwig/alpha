import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# def submit():
#     day = day_entry.get()
#     month = month_entry.get()
#     year = year_entry.get()

#     # Validate the input (you can add more specific validation)
#     if not day.isdigit() or not month.isdigit() or not year.isdigit():
#         messagebox.showerror("Error", "Please enter valid numbers for day, month, and year.")
#         return

#     # Assuming a valid date format (you can add more extensive date validation)
#     birthday = f"{day}/{month}/{year}"
#     messagebox.showinfo("Birthday", f"Thank you! Your birthday is: {birthday}")

def submit():
    day = day_entry.get()
    month = month_entry.get()
    year = year_entry.get()

    # Validate the input (you can add more specific validation)
    if not day.isdigit() or not month.isdigit() or not year.isdigit():
        messagebox.showerror("Error", "Please enter valid numbers for day, month, and year.")
        return

    # Assuming a valid date format (you can add more extensive date validation)
    birthday = f"{day}/{month}/{year}"
    messagebox.showinfo("Birthday", f"Thank you! Your birthday is: {birthday}")

root = tk.Tk()
root.title("Birthday Form")

# Create labels and entry fields for day, month, and year
day_label = ttk.Label(root, text="Day:")
day_label.grid(row=0, column=0, padx=10, pady=5)

day_entry = ttk.Entry(root)
day_entry.grid(row=0, column=1, padx=10, pady=5)

month_label = ttk.Label(root, text="Month:")
month_label.grid(row=1, column=0, padx=10, pady=5)

month_entry = ttk.Entry(root)
month_entry.grid(row=1, column=1, padx=10, pady=5)

year_label = ttk.Label(root, text="Year:")
year_label.grid(row=2, column=0, padx=10, pady=5)

year_entry = ttk.Entry(root)
year_entry.grid(row=2, column=1, padx=10, pady=5)

# Create a submit button
submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()



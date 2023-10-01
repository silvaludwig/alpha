import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    day = day_entry.get()
    month = month_entry.get()
    year = year_entry.get()
    email = email_entry.get()
    address = address_text.get("1.0", "end-1c")

    # Validate the input (you can add more specific validation)
    if not first_name or not last_name or not day.isdigit() or not month.isdigit() \
            or not year.isdigit() or not email:
        messagebox.showerror("Error", "Please fill in all fields with valid information.")
        return

    # Assuming a valid date format (you can add more extensive date validation)
    birthday = f"{day}/{month}/{year}"

    # Display collected information in a message box
    info_message = f"Name: {first_name} {last_name}\nBirthday: {birthday}\nEmail: {email}\nAddress: {address}"
    messagebox.showinfo("Collected Information", info_message)

root = tk.Tk()
root.title("Personal Information Form")

# Create labels and entry fields for name, last name, birthday, email, and address
first_name_label = ttk.Label(root, text="First Name:")
first_name_label.grid(row=0, column=0, padx=10, pady=5)

first_name_entry = ttk.Entry(root)
first_name_entry.grid(row=0, column=1, padx=10, pady=5)

last_name_label = ttk.Label(root, text="Last Name:")
last_name_label.grid(row=1, column=0, padx=10, pady=5)

last_name_entry = ttk.Entry(root)
last_name_entry.grid(row=1, column=1, padx=10, pady=5)

birthday_label = ttk.Label(root, text="Birthday (DD/MM/YYYY):")
birthday_label.grid(row=2, column=0, padx=10, pady=5)

day_entry = ttk.Entry(root, width=5)
day_entry.grid(row=2, column=1, padx=5, pady=5)

month_entry = ttk.Entry(root, width=5)
month_entry.grid(row=2, column=2, padx=5, pady=5)

year_entry = ttk.Entry(root, width=7)
year_entry.grid(row=2, column=3, padx=5, pady=5)

email_label = ttk.Label(root, text="Email:")
email_label.grid(row=3, column=0, padx=10, pady=5)

email_entry = ttk.Entry(root)
email_entry.grid(row=3, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

address_label = ttk.Label(root, text="Address:")
address_label.grid(row=4, column=0, padx=10, pady=5)

address_text = tk.Text(root, height=5, width=30)
address_text.grid(row=4, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

# Create a submit button
submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()

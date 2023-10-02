import tkinter as tk
from tkinter import ttk

def select_day():
    select_day = combo_var.get()

def select_month():
    select_month = combo_var.get()

def select_year():
    select_year = combo_var.get()

# Create the main application window
root = tk.Tk()
root.title("Select Menu Example")

# Create a Combobox widget
options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
combo_var = tk.StringVar()
combo = ttk.Combobox(root, textvariable=combo_var, values=options)
combo.grid(row=1, column=0, padx=10, pady=10)

# Create a button to get the selected option
get_option_button = ttk.Button(root, text="Get Selected Option", command=select_day)
get_option_button.grid(row=2, column=0, padx=10, pady=10)

# Create a label to display the selected option
selected_option_label = ttk.Label(root, text="Day")
selected_option_label.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()

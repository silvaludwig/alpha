from income import Income
from expense import Expense
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

main_window = Tk()
main_window.title('Money Manager')

class Main():

    def access_income():
        income_instance = Income()
        income_instance()

    # Function to create an instance of Class2
    def access_expense():
        expense_instance = Expense()
        expense_instance()

# Create buttons to access the classes
button1 = tk.Button(main_window, text="New Income", command=Main.access_income)
button1.pack()

button2 = tk.Button(main_window, text="New Expense", command=Main.access_expense)
button2.pack()

main_window.mainloop()

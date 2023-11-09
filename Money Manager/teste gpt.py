# # import tkinter as tk
# # from tkinter import ttk

# # class FinancialManager:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("Financial Manager")

# #         self.incomes = []
# #         self.expenses = []

# #         # Create labels
# #         ttk.Label(root, text="Income").grid(row=0, column=0, padx=10, pady=10)
# #         ttk.Label(root, text="Amount").grid(row=0, column=1, padx=10, pady=10)
# #         ttk.Label(root, text="Expense").grid(row=2, column=0, padx=10, pady=10)
# #         ttk.Label(root, text="Amount").grid(row=2, column=1, padx=10, pady=10)

# #         # Create entry fields
# #         self.income_entry = ttk.Entry(root)
# #         self.income_entry.grid(row=1, column=0, padx=10, pady=10)
# #         self.amount_entry = ttk.Entry(root)
# #         self.amount_entry.grid(row=1, column=1, padx=10, pady=10)
# #         self.expense_entry = ttk.Entry(root)
# #         self.expense_entry.grid(row=3, column=0, padx=10, pady=10)
# #         self.expense_amount_entry = ttk.Entry(root)
# #         self.expense_amount_entry.grid(row=3, column=1, padx=10, pady=10)

# #         # Create buttons
# #         ttk.Button(root, text="Add Income", command=self.add_income).grid(row=1, column=2, padx=10, pady=10)
# #         ttk.Button(root, text="Add Expense", command=self.add_expense).grid(row=3, column=2, padx=10, pady=10)

# #         # Create listboxes to display incomes and expenses
# #         self.income_listbox = tk.Listbox(root)
# #         self.income_listbox.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
# #         self.expense_listbox = tk.Listbox(root)
# #         self.expense_listbox.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# #     def add_income(self):
# #         income = self.income_entry.get()
# #         amount = self.amount_entry.get()
# #         if income and amount:
# #             self.incomes.append((income, amount))
# #             self.update_income_listbox()
# #             self.income_entry.delete(0, tk.END)
# #             self.amount_entry.delete(0, tk.END)

# #     def add_expense(self):
# #         expense = self.expense_entry.get()
# #         amount = self.expense_amount_entry.get()
# #         if expense and amount:
# #             self.expenses.append((expense, amount))
# #             self.update_expense_listbox()
# #             self.expense_entry.delete(0, tk.END)
# #             self.expense_amount_entry.delete(0, tk.END)

# #     def update_income_listbox(self):
# #         self.income_listbox.delete(0, tk.END)
# #         for income, amount in self.incomes:
# #             self.income_listbox.insert(tk.END, f"{income}: ${amount}")

# #     def update_expense_listbox(self):
# #         self.expense_listbox.delete(0, tk.END)
# #         for expense, amount in self.expenses:
# #             self.expense_listbox.insert(tk.END, f"{expense}: ${amount}")

# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = FinancialManager(root)
# #     root.mainloop()






# #Import the required libraries
# from tkinter import *
# from tkinter import ttk

# #Create an instance of Tkinter Frame
# win = Tk()

# #Set the geometry
# win.geometry("700x250")

# # Define a function to return the Input data
# def get_data():
#    label.config(text= entry.get(), font= ('Helvetica 13'))

# #Create an Entry Widget
# entry = Entry(win, width= 42)
# entry.place(relx= .5, rely= .5, anchor= CENTER)

# #Inititalize a Label widget
# label= Label(win, text="", font=('Helvetica 13'))
# label.pack()

# #Create a Button to get the input data
# ttk.Button(win, text= "Click to Show", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)

# win.mainloop()
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

class Window1:
    def __init__(self, root):
        self.root = root
        self.root.title("New Income")

        self.income_discrimination_label = ttk.Label(self.root, text='Discrimination: ')
        self.income_discrimination_label.grid(column=0, row=0)
        self.income_discrimination_entry = ttk.Entry(self.root)
        self.income_discrimination_entry.grid(column=1, row=0)

        self.income_value_label = ttk.Label(self.root, text='Value: ')
        self.income_value_label.grid(column=0, row=1)
        self.income_value_entry = ttk.Entry(self.root)
        self.income_value_entry.grid(column=1, row=1)

        self.income_recurrent_label = ttk.Label(self.root, text='Is it recurrent? ')
        self.income_recurrent_label.grid(column=0, row=2)
        self.income_recurrent_options = ['Non Recurrent', 'Weekly', 'Monthly']
        self.income_recurrent_var = tk.StringVar()
        self.recurrent = ttk.Combobox(self.root, values=self.income_recurrent_options, textvariable=self.income_recurrent_var)
        self.recurrent.grid(column=1, row=2)

        self.income_date_day_label = ttk.Label(self.root, text='Day')
        self.income_date_day_label.grid(column=0, row=3)
        self.income_date_day_options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        self.income_date_day_var = tk.StringVar()
        self.day = ttk.Combobox(self.root, values=self.income_date_day_options, textvariable=self.income_date_day_var)
        self.day.grid(column=1, row=3)

        self.income_date_month_label = ttk.Label(self.root, text='Month')
        self.income_date_month_label.grid(column=0, row=4)
        self.income_date_month_options = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.income_date_month_var = tk.StringVar()
        self.month = ttk.Combobox(self.root, values=self.income_date_month_options, textvariable=self.income_date_month_var)
        self.month.grid(column=1, row=4)

        self.income_date_year_label = ttk.Label(self.root, text='Year')
        self.income_date_year_label.grid(column=0, row=5)
        self.income_date_year_options = [2020, 2021, 2022, 2023, 2024]
        self.income_date_year_var = tk.StringVar()
        self.year = ttk.Combobox(self.root, values=self.income_date_year_options, textvariable=self.income_date_year_var)
        self.year.grid(column=1, row=5)

        self.income_category_var_label = ttk.Label(self.root, text='Category')
        self.income_category_var_label.grid(column=0, row=6)
        self.income_category_var_options = ['House', 'Car', 'Health', 'Pets', 'Taxes', 'Misc']
        self.income_category_var = tk.StringVar()
        self.category = ttk.Combobox(self.root, values=self.income_category_var_options, textvariable=self.income_category_var)
        self.category.grid(column=1, row=6)

        self.income_account_entry_label = ttk.Label(self.root, text='Account')
        self.income_account_entry_label.grid(column=0, row=7)
        self.income_account_var_options = ['Neon', 'Nubank', 'Nubank PJ', 'CEF', 'C6', 'C6 PJ', 'Wallet']
        self.income_account_var = tk.StringVar()
        self.account = ttk.Combobox(self.root, values=self.income_account_var_options, textvariable=self.income_account_var)
        self.account.grid(column=1, row=7)

        def submit():
                    print('New income registered successfuly!')
                    print(f'Discrimination: {self.income_discrimination_entry.get()}')
                    print(f'Value: R${self.income_value_entry.get()}')
                    print(f'Date: {self.income_date_day_var.get()}/{self.income_date_month_var.get()}/{self.income_date_year_var.get()}')        
                    print(f'Recurrency: {self.income_recurrent_var.get()}')
                    print(f'Category: {self.income_category_var.get()}')
                    print(f'Account: {self.income_account_var.get()}')

        self.submit_button = tk.Button(root, text="Submit", command=submit)
        self.submit_button.grid(column=0, row=8)

        self.quit_button = tk.Button(root, text='Quit', command=quit)
        self.quit_button.grid(column=1, row=8)

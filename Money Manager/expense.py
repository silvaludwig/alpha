from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter


class Expense:
    
    def __init__(self, source, value, recurrent, category, account):
        self.source = expense_discrimination_entry.get()
        self.value = expense_value_entry.get()
        self.recurrent = expense_recurrent_var.get()
        self.category = expense_category_var.get()
        self.account = expense_account_var.get()

    def submit():
            print('New expense registered successfuly!')
            print(f'Discrimination: {expense_discrimination_entry.get()}')
            print(f'Value: R${expense_value_entry.get()}')
            print(f'Date: {expense_date_day_var.get()}/{expense_date_month_var.get()}/{expense_date_year_var.get()}')        
            print(f'Recurrency: {expense_recurrent_var.get()}')
            print(f'Category: {expense_category_var.get()}')
            print(f'Account: {expense_account_var.get()}')

    # print(f'Source: {expense_discrimination_entry}, Value: R${expense_value_entry}, Recurrent: {expense_recurrent_var}, \n Category: {expense_category_var}, Account: {expense_account_var} \n New expense registered successfuly!')


window = Tk()
window.title('New expense')

expense_discrimination_label = ttk.Label(window, text='Discrimination: ')
expense_discrimination_label.grid(column=0, row=0)
expense_discrimination_entry = ttk.Entry(window)
expense_discrimination_entry.grid(column=1, row=0)

expense_value_label = ttk.Label(window, text='Value: ')
expense_value_label.grid(column=0, row=1)
expense_value_entry = ttk.Entry(window)
expense_value_entry.grid(column=1, row=1)

expense_recurrent_label = ttk.Label(window, text='Is it recurrent? ')
expense_recurrent_label.grid(column=0, row=2)
expense_recurrent_options = ['Non Recurrent', 'Weekly', 'Monthly']
expense_recurrent_var = tkinter.StringVar()
recurrent = ttk.Combobox(window, values=expense_recurrent_options, textvariable=expense_recurrent_var)
recurrent.grid(column=1, row=2)

expense_date_day_label = ttk.Label(window, text='Day')
expense_date_day_label.grid(column=0, row=3)
expense_date_day_options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
expense_date_day_var = tkinter.StringVar()
day = ttk.Combobox(window, values=expense_date_day_options, textvariable=expense_date_day_var)
day.grid(column=1, row=3)

expense_date_month_label = ttk.Label(window, text='Month')
expense_date_month_label.grid(column=0, row=4)
expense_date_month_options = [1,2,3,4,5,6,7,8,9,10,11,12]
expense_date_month_var = tkinter.StringVar()
month = ttk.Combobox(window, values=expense_date_month_options, textvariable=expense_date_month_var)
month.grid(column=1, row=4)

expense_date_year_label = ttk.Label(window, text='Year')
expense_date_year_label.grid(column=0, row=5)
expense_date_year_options = [2020, 2021, 2022, 2023, 2024]
expense_date_year_var = tkinter.StringVar()
year = ttk.Combobox(window, values=expense_date_year_options, textvariable=expense_date_year_var)
year.grid(column=1, row=5)

expense_category_var_label = ttk.Label(window, text='Category')
expense_category_var_label.grid(column=0, row=6)
expense_category_var_options = ['House', 'Car', 'Health', 'Pets', 'Taxes', 'Misc']
expense_category_var = tkinter.StringVar()
category = ttk.Combobox(window, values=expense_category_var_options, textvariable=expense_category_var)
category.grid(column=1, row=6)

expense_account_entry_label = ttk.Label(window, text='Account')
expense_account_entry_label.grid(column=0, row=7)
expense_account_var_options = ['Neon', 'Nubank', 'Nubank PJ', 'CEF', 'C6', 'C6 PJ', 'Wallet']
expense_account_var = tkinter.StringVar()
account = ttk.Combobox(window, values=expense_account_var_options, textvariable=expense_account_var)
account.grid(column=1, row=7)

# submit button
submit_button = ttk.Button(window, text='Submit', command= Expense.submit)
submit_button.grid(column=0, row=8, padx=10, pady=5)

quit_button = ttk.Button(window, text='Quit', command=window.destroy)
quit_button.grid(column=1, row=8)


window.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter


class Income:
    def __init__(self):
        self = self

    def get_income():
        source = income_discrimination_entry.get()
        value = income_value_entry.get()
        recurrent = income_recurrent_var.get()
        category = income_category_var.get()
        account = income_account_var.get()

    def submit():
            print('New income registered successfuly!')
            print(f'Discrimination: {income_discrimination_entry.get()}')
            print(f'Value: R${income_value_entry.get()}')
            print(f'Date: {income_date_day_var.get()}/{income_date_month_var.get()}/{income_date_year_var.get()}')        
            print(f'Recurrency: {income_recurrent_var.get()}')
            print(f'Category: {income_category_var.get()}')
            print(f'Account: {income_account_var.get()}')

    # print(f'Source: {income_discrimination_entry}, Value: R${income_value_entry}, Recurrent: {income_recurrent_var}, \n Category: {income_category_var}, Account: {income_account_var} \n New income registered successfuly!')


inc_window = Tk()
inc_window.title('New Income')

income_discrimination_label = ttk.Label(inc_window, text='Discrimination: ')
income_discrimination_label.grid(column=0, row=0)
income_discrimination_entry = ttk.Entry(inc_window)
income_discrimination_entry.grid(column=1, row=0)

income_value_label = ttk.Label(inc_window, text='Value: ')
income_value_label.grid(column=0, row=1)
income_value_entry = ttk.Entry(inc_window)
income_value_entry.grid(column=1, row=1)

income_recurrent_label = ttk.Label(inc_window, text='Is it recurrent? ')
income_recurrent_label.grid(column=0, row=2)
income_recurrent_options = ['Non Recurrent', 'Weekly', 'Monthly']
income_recurrent_var = tkinter.StringVar()
recurrent = ttk.Combobox(inc_window, values=income_recurrent_options, textvariable=income_recurrent_var)
recurrent.grid(column=1, row=2)

income_date_day_label = ttk.Label(inc_window, text='Day')
income_date_day_label.grid(column=0, row=3)
income_date_day_options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
income_date_day_var = tkinter.StringVar()
day = ttk.Combobox(inc_window, values=income_date_day_options, textvariable=income_date_day_var)
day.grid(column=1, row=3)

income_date_month_label = ttk.Label(inc_window, text='Month')
income_date_month_label.grid(column=0, row=4)
income_date_month_options = [1,2,3,4,5,6,7,8,9,10,11,12]
income_date_month_var = tkinter.StringVar()
month = ttk.Combobox(inc_window, values=income_date_month_options, textvariable=income_date_month_var)
month.grid(column=1, row=4)

income_date_year_label = ttk.Label(inc_window, text='Year')
income_date_year_label.grid(column=0, row=5)
income_date_year_options = [2020, 2021, 2022, 2023, 2024]
income_date_year_var = tkinter.StringVar()
year = ttk.Combobox(inc_window, values=income_date_year_options, textvariable=income_date_year_var)
year.grid(column=1, row=5)

income_category_var_label = ttk.Label(inc_window, text='Category')
income_category_var_label.grid(column=0, row=6)
income_category_var_options = ['House', 'Car', 'Health', 'Pets', 'Taxes', 'Misc']
income_category_var = tkinter.StringVar()
category = ttk.Combobox(inc_window, values=income_category_var_options, textvariable=income_category_var)
category.grid(column=1, row=6)

income_account_entry_label = ttk.Label(inc_window, text='Account')
income_account_entry_label.grid(column=0, row=7)
income_account_var_options = ['Neon', 'Nubank', 'Nubank PJ', 'CEF', 'C6', 'C6 PJ', 'Wallet']
income_account_var = tkinter.StringVar()
account = ttk.Combobox(inc_window, values=income_account_var_options, textvariable=income_account_var)
account.grid(column=1, row=7)

# submit button
submit_button = ttk.Button(inc_window, text='Submit', command= Income.submit)
submit_button.grid(column=0, row=8, padx=10, pady=5)

quit_button = ttk.Button(inc_window, text='Quit', command=inc_window.destroy)
quit_button.grid(column=1, row=8)


inc_window.mainloop()

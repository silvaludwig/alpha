from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter


class Income:
    def __init__(self, source, value, recurrent, category, account):
        self.source = income_discrimination_entry.get()
        self.value = income_value_entry.get()
        self.recurrent = income_recurrent_var.get()
        self.category = income_category_var.get()
        self.account = income_account_var.get()

window = Tk()
window.title('New Income')
# frame = ttk.Frame(window, padding=10)
# frame.grid()

income_discrimination_label = ttk.Label(window, text='Discrimination: ')
income_discrimination_label.grid(column=0, row=0)
income_discrimination_entry = ttk.Entry(window)
income_discrimination_entry.grid(column=1, row=0)

income_value_label = ttk.Label(window, text='Value: ')
income_value_label.grid(column=0, row=1)
income_value_entry = ttk.Entry(window)
income_value_entry.grid(column=1, row=1)

income_recurrent_label = ttk.Label(window, text='Is it recurrent? ')
income_recurrent_label.grid(column=0, row=2)
income_recurrent_options = ['Non Recurrent', 'Weekly', 'Monthly']
income_recurrent_var = tkinter.StringVar()
recurrent = ttk.Combobox(window, values=income_recurrent_options, textvariable=income_recurrent_var)
recurrent.grid(column=1, row=2)

income_date_day_label = ttk.Label(window, text='Day')
income_date_day_label.grid(column=0, row=3)
income_date_day_options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
income_date_day_var = tkinter.StringVar()
day = ttk.Combobox(window, values=income_date_day_options, textvariable=income_date_day_var)
day.grid(column=1, row=3)

income_date_month_label = ttk.Label(window, text='Month')
income_date_month_label.grid(column=0, row=4)
income_date_month_options = [1,2,3,4,5,6,7,8,9,10,11,12]
income_date_month_var = tkinter.StringVar()
month = ttk.Combobox(window, values=income_date_month_options, textvariable=income_date_month_var)
month.grid(column=1, row=4)

income_date_year_label = ttk.Label(window, text='Year')
income_date_year_label.grid(column=0, row=5)
income_date_year_entry = ttk.Entry(window)
income_date_year_entry.grid(column=1, row=5)




window.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter


def new_user():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    gender = gender_var.get()
    job = job_entry.get()
    birth_day = days_var.get()
    birth_month = month_var.get()
    birth_year = birth_year_entry.get()
    address_first_line = address_first_line_entry.get()
    address_city = address_city_entry.get()
    address_state = address_state_entry.get()
    address_country = address_country_entry.get()
    phone_number = phone_number_entry.get()
    email = email_entry.get()


# validating if the inputs are empty
    if not first_name or not last_name or not job or not birth_year.isdigit() or not address_first_line or not address_country or not address_city \
            or not phone_number.isdigit() or not email:
        messagebox.showerror('Attention!', 'Please fill all fields with valid data!')

# validating the inputs that can't be only numbers)
    elif first_name.isdigit() or last_name.isdigit() or address_city.isdigit() or address_state.isdigit() or address_country.isdigit() or job.isdigit():
        messagebox.showerror('Attention!', 'Invalid Data!')
        if first_name.isdigit():
            messagebox.showerror('Attention!', 'Invalid First Name!')
            first_name_entry.delete(0, END)
        elif last_name.isdigit():
            messagebox.showerror('Attention!', 'Invalid Last Name!')
            last_name_entry.delete(0, END)
        elif job.isdigit():
            messagebox.showerror('Attention!', 'Invalid Job!')
            job_entry.delete(0, END)
        elif address_city.isdigit():
            messagebox.showerror('Attention!', 'Invalid City!')
            address_city_entry.delete(0, END)
        elif address_state.isdigit():
            messagebox.showerror('Attention!', 'Invalid State!')
            address_state_entry.delete(0, END)
        elif address_country.isdigit():
            messagebox.showerror('Attention!', 'Invalid Country!')
            address_country_entry.delete(0, END)
            
    else:
        messagebox.showinfo('System', 'Registered successfuly!')
        response = messagebox.askquestion('Another Registration', 'Do You Want to Make another Registration?')
        if response == 'yes':
                first_name_entry.delete(0, END)
                last_name_entry.delete(0, END)
                gender_var.set('')
                job_entry.delete(0, END)
                days_var.set('')
                month_var.set('')
                birth_year_entry.delete(0, END)
                address_first_line_entry.delete(0, END)
                address_city_entry.delete(0, END)
                address_state_entry.delete(0, END)
                address_country_entry.delete(0, END)
                phone_number_entry.delete(0, END)
                email_entry.delete(0, END)
        else:
            janela.destroy()


janela = Tk()
janela.title('Personal Info')
moldura = ttk.Frame(janela, padding=10)
moldura.grid()

# labels and entrys
first_name_label = ttk.Label(janela, text='First Name')
first_name_label.grid(column=0, row=0, padx=10, pady=5)

first_name_entry = ttk.Entry(janela)
first_name_entry.grid(column=1, row=0, padx=10, pady=5)

last_name_label = ttk.Label(janela, text='Last Name')
last_name_label.grid(column=2, row=0, padx=10, pady=5)

last_name_entry = ttk.Entry(janela)
last_name_entry.grid(column=3, row=0, padx=10, pady=5)

# creating a combobox for the day
day_label = ttk.Label(janela, text= 'Birthday')
day_label.grid(column=5, row=0)

days_options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
days_var = tkinter.StringVar()
days = ttk.Combobox(janela, width=5, textvariable=days_var, values=days_options)
days.grid(column=6, row=0)

# creating a combobox for month, year and gender
month_label = ttk.Label(janela, text= 'Month')
month_label.grid(column=7, row=0)

month_options = [1,2,3,4,5,6,7,8,9,10,11,12]
month_var = tkinter.StringVar()
month = ttk.Combobox(janela, width=5, textvariable=month_var, values=month_options)
month.grid(column=8, row=0)

birth_year_label = ttk.Label(janela, text= 'Year')
birth_year_label.grid(column=9, row=0)

birth_year_entry = ttk.Entry(janela, width=7)
birth_year_entry.grid(column=10, row=0)

gender_label = ttk.Label(janela, text='Gender')
gender_label.grid(column=0, row=2, padx=10, pady=5)

gender_options = ['Male', 'Female']
gender_var = tkinter.StringVar()
gender = ttk.Combobox(janela, textvariable=gender_var, values=gender_options)
gender.grid(column=1, row=2)

job_label = ttk.Label(janela, text='Job')
job_label.grid(column=2, row=2, padx=10, pady=5)

job_entry = ttk.Entry(janela)
job_entry.grid(column=3, row=2, padx=10, pady=5)

address_first_line_label = ttk.Label(janela, text = 'Address')
address_first_line_label.grid(column=0, row=5, padx=10, pady=5)

address_first_line_entry = ttk.Entry(janela)
address_first_line_entry.grid(column=1, row=5, padx=10, pady=5)

address_city_label = ttk.Label(janela, text='City')
address_city_label.grid(column=2, row=5, padx=10, pady=5)

address_city_entry = ttk.Entry(janela)
address_city_entry.grid(column=3, row=5, padx=10, pady=5)

address_state_label = ttk.Label(janela, text='State')
address_state_label.grid(column=0, row=6, padx=10, pady=5)

address_state_entry = ttk.Entry(janela)
address_state_entry.grid(column=1, row=6, padx=10, pady=5)

address_country_label = ttk.Label(janela, text='Country')
address_country_label.grid(column=2, row=6, padx=10, pady=5)

address_country_entry = ttk.Entry(janela)
address_country_entry.grid(column=3, row=6, padx=10, pady=5)

phone_number_label = ttk.Label(janela, text='Phone Number')
phone_number_label.grid(column=0, row=7, padx=10, pady=5)

phone_number_entry = ttk.Entry(janela)
phone_number_entry.grid(column=1, row=7, padx=10, pady=5)

email_label = ttk.Label(janela, text='E-mail')
email_label.grid(column=2, row=7, padx=10, pady=5)

email_entry = ttk.Entry(janela)
email_entry.grid(column=3, row=7, padx=10, pady=5)

# submit button
submit_button = ttk.Button(janela, text='Submit', command= new_user)
submit_button.grid(column=1, row=12, padx=10, pady=5)

def clear_form():
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    job_entry.delete(0, END)
    gender_var.set('')
    days_var.set('')
    month_var.set('')
    birth_year_entry.delete(0, END)
    address_first_line_entry.delete(0, END)
    address_city_entry.delete(0, END)
    address_state_entry.delete(0, END)
    address_country_entry.delete(0, END)
    phone_number_entry.delete(0, END)
    email_entry.delete(0, END)

# clear end quit buttons
clear_button = ttk.Button(janela, text='Clear', command=clear_form)
clear_button.grid(column=2, row=12)

quit_button = ttk.Button(janela, text='Quit', command=janela.destroy)
quit_button.grid(column=3, row=12)

janela.mainloop()
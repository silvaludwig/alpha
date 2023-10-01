from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def new_user():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    gender = gender_entry.get()
    job = job_entry.get()
    birth_day = birth_day_entry.get()
    birth_month = birth_month_entry.get()
    birth_year = birth_year_entry.get()
    address_first_line = address_first_line_entry.get()
    address_city = address_city_entry.get()
    address_state = address_state_entry.get()
    address_country = address_country_entry.get()
    phone_number = phone_number_entry.get()
    email = email_entry.get()

# validating the inputs
    if not first_name or not last_name or not job or not birth_day.isdigit() or not birth_month.isdigit() \
            or not birth_year.isdigit() or not address_first_line or not address_country or not address_city \
            or not phone_number.isdigit() or not email or not gender:
        messagebox.showerror('Error', 'Please fill all fields')
    # if birth_month == 2 and birth_day > 28:
    #     messagebox.ERROR('Error', 'Please fill witha valid data')
    else:
        messagebox.showinfo('System', 'Registered successfuly!')    




janela = Tk()
janela.title('Personal Info Form')
moldura = ttk.Frame(janela, padding=10)
moldura.grid()
# ttk.Label(moldura, text='Teste de criação de interface').grid(column=0, row=0)

# labels and entrys
first_name_label = ttk.Label(janela, text='First Name')
first_name_label.grid(column=0, row=0, padx=10, pady=5)

first_name_entry = ttk.Entry(janela)
first_name_entry.grid(column=1, row=0, padx=10, pady=5)

last_name_label = ttk.Label(janela, text='Last Name')
last_name_label.grid(column=0, row=1, padx=10, pady=5)

last_name_entry = ttk.Entry(janela)
last_name_entry.grid(column=1, row=1, padx=10, pady=5)

gender_label = ttk.Label(janela, text='Gender')
gender_label.grid(column=0, row=2, padx=10, pady=5)

gender_entry = ttk.Entry(janela)
gender_entry.grid(column=1, row=2, padx=10, pady= 5)

job_label = ttk.Label(janela, text='Job')
job_label.grid(column=0, row=3, padx=10, pady=5)

job_entry = ttk.Entry(janela)
job_entry.grid(column=1, row=3, padx=10, pady=5)

birthday_label = ttk.Label(janela, text= 'Birthday [DD/MM/YYYY]')
birthday_label.grid(column=0, row=4, padx=10, pady=5)

# birth_day_label = ttk.Label(janela)
# birth_day_label.grid(column=0, row=4, padx=10, pady=5)

birth_day_entry = ttk.Entry(janela, width=5)
birth_day_entry.grid(column=1, row=4, padx=5, pady=5)

# birth_month_label = ttk.Label(janela)
# birth_month_label.grid(column=2, row=4, padx=10, pady=5)

birth_month_entry = ttk.Entry(janela, width=5)
birth_month_entry.grid(column=2, row=4, padx=5, pady=5)

# birth_year_label = ttk.Label(janela, text= 'Day')
# birth_year_label.grid(column=3, row=4, padx=10, pady=5)

birth_year_entry = ttk.Entry(janela, width=7)
birth_year_entry.grid(column=3, row=4, padx=7, pady=5)

address_first_line_label = ttk.Label(janela, text = 'Address')
address_first_line_label.grid(column=0, row=5, padx=10, pady=5)

address_first_line_entry = ttk.Entry(janela)
address_first_line_entry.grid(column=1, row=5, padx=10, pady=5)

address_city_label = ttk.Label(janela, text='City')
address_city_label.grid(column=0, row=6, padx=10, pady=5)

address_city_entry = ttk.Entry(janela)
address_city_entry.grid(column=1, row=6, padx=10, pady=5)

address_state_label = ttk.Label(janela, text='State')
address_state_label.grid(column=0, row=7, padx=10, pady=5)

address_state_entry = ttk.Entry(janela)
address_state_entry.grid(column=1, row=7, padx=10, pady=5)

address_country_label = ttk.Label(janela, text='Country')
address_country_label.grid(column=0, row=8, padx=10, pady=5)

address_country_entry = ttk.Entry(janela)
address_country_entry.grid(column=1, row=8, padx=10, pady=5)

phone_number_label = ttk.Label(janela, text='Phone Number [(XX) X XXXX-XXXX]')
phone_number_label.grid(column=0, row=9, padx=10, pady=5)

phone_number_entry = ttk.Entry(janela)
phone_number_entry.grid(column=1, row=9, padx=10, pady=5)

email_label = ttk.Label(janela, text='E-mail')
email_label.grid(column=0, row=10, padx=10, pady=5)

email_entry = ttk.Entry(janela)
email_entry.grid(column=1, row=10, padx=10, pady=5)

# submit button
submit_button = ttk.Button(janela, text='Submit', command= new_user)
submit_button.grid(column=1, row=12, padx=10, pady=5)


# ttk.Button(janela, text='Fim do programa', command=janela.destroy).grid(column=0, row=2)

janela.mainloop()

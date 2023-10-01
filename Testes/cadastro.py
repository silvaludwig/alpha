print('#' *15)
print('   New User')
print('#' *15)
concluded = False
while not concluded:
     first_name = str(input('First Name: ')).strip().upper()
     last_name = str(input('Last Name: ')).strip().upper()
     gender = str(input('Gender [M/F]: ')).strip().upper()
     while gender not in 'MmFf':
          print('Try again')
          gender = str(input('Gender [M/F]: ')).strip().upper()
     email = str(input('E-mail: ')).strip().upper()
     # birth_day = str(input('Day: '))
     address = str(input('Address: ')).strip().upper()
     address_city = str(input('City: ')).strip().upper()
     address_state = str(input('State: ')).strip().upper()
     address_country = str(input('Country: ')).strip().upper()
     register = str(input('Another register? [Y/N] ')).strip().upper()
     if register in 'Nn':
          concluded = True
     elif register not in 'YyNn':
          print('Invalid')
     else: 
          print('New register')
          print('#'*15)
print('Successfully registered')
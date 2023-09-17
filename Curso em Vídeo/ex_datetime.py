import datetime
from datetime import timedelta

current_datetime = datetime.datetime.now()
print(current_datetime)

year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
hour = current_datetime.hour
minute = current_datetime.minute

current_time = '{:02}:{:02}' . format(hour, minute)

x = str(input('Pergunte a data ou a hora: '))
match x:
    case 'data':  
        print('Data: {:02}/{:02}/{}' .format(day, month, year))
    case 'hora':
        print('Horário local: ', current_time)


# tentar fazer um programa que mostre o horário
# em outro fuso


x2 = input('gostaria de saber o horário da china? ')
if x2 == 'sim':
    print(current_time + timedelta(hours=11))
else: 
    print('vai se lascar então')

print('fim do programa')
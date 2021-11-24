import datetime

my_time = datetime.datetime.now()

print(my_time)
print(f'Year: {my_time.year}')
print(f'Month: {my_time.month}')
print(f'Day: {my_time.day}')
print(f'Format LATAM: {my_time.strftime("%d/%m/%Y")}')
print(f'Format USA: {my_time.strftime("%m/%d/%Y")}')
print(f'Format Random: {my_time.strftime("Actual hour is %H:%M:%S")}')



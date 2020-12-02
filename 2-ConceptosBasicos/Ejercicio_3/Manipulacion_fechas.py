import datetime

print('¿Cuántos días tienes de vida?')
day = int(input('Introduce el día en que naciste\n'))
month = int(input('Introduce el mes en que naciste\n'))
year = int(input('Introduce el año en que naciste\n'))
birthday =  datetime.datetime(year, month, day)
today = datetime.datetime.now()
diff = today - birthday
print(f'Tienes {diff.days} días de vida')
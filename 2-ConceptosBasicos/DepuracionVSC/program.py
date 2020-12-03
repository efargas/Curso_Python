import datetime
def años(fecha):
    """
    Programa que calcula cuantos años han pasado con una fecha.
    """
    ahora = datetime.date.today()
    return ahora.year - fecha
if __name__ == '__main__':
    a = 2012
    resultado = años(a)
    print(f'Hace {resultado} años de la fecha proporcionada')
print('Cuenta números pares')
i = 0

while True:
    num = int(input('Escriba un número par: '))
    if num % 2 == 0:
        i +=1
        if input('Quieres escribir otro número par? (S/N): ').lower() != 's':
            break
    else:
        print(f'{num} no es un número par. Inténtalo de nuevo')
print(f'Has escrito {i} números pares.')
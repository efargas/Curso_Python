print('Script que encuentra múltiplos')
num1 = int(input('Introduce un número entero: '))
num2 = int(input('Introduce otro número entero: '))

if (num1 % num2) == 0 or (num2 % num1) == 0:
    if num1 == num2:
        print(f'{num1} es múltiplo de {num2}')
    elif num1 > num2:
        print(f'{num1} es múltiplo de {num2}')
    else:
        print(f'{num2} es múltiplo de {num1}')
else:
    if num1 > num2:
        print(f'{num1} No es múltiplo de {num2}')
    else:
        print(f'{num2} No es múltiplo de {num1}')

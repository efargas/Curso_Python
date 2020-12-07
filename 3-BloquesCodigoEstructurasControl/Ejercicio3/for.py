print('Suma entre valores')
num1 = int(input('Escribe un número entero positivo: '))
num2 = 0
f = []
suma = 0
formula = ''
if num1 < 0:
    print('¡Te he pedido un número entero positivo!')
else:
    num2 = int(input(f'Escribe un número entero mayor que {num1}: '))
    if num1 >= num2:
        print(f'Te he pedido un número mayor que {num1}')
    else:
        for n in range (num1,num2+1):
            if n < num2:
                f.append(n)
                f.append(' + ')
            else:
                f.append(n)
                f.append(' = ')
            suma = suma + n
    f.append(suma)
print(f'La suma desde {num1} hasta {num2} es {suma}')

for i in range (0,len(f)):
    formula = formula + str(f[i])

print(formula)
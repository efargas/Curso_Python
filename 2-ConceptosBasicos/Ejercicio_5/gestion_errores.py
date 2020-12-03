'''
Calculadora que solo suma, por ahora.
'''

print('Calculadora que suma')

def suma(n1,n2): return n1+n2

valor1 = input('Introduce el primer valor: ')
valor2 = input('Introduce el segundo valor: ')

try:
    resultado = suma(float(valor1),float(valor2))
    print(f'La suma es: {resultado}')

    resultado2 = suma(float(valor1),valor2) #Error de tipos float + string
    print(f'La suma es: {resultado2}')

except ValueError as mensaje:
    print('Error: El valor debe ser un número')
    print(mensaje)
except TypeError as mensaje:
    print('Error: El tipo de dato ha de ser float')
    print(mensaje)
finally:
    print('Fin del programa')

try:
    sum = lambda a,b: float(a)+float(b)
    print(sum(input('Introduce el primer valor: '),input('Introduce el segundo valor: ')))
except ValueError as mensaje:
    print('Error: El valor debe ser un número')
    print(mensaje)
finally:
    print('Prueba con función lambda')
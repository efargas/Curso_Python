num = int(input('Introduce un valor para saber su factorial: '))

def factorial(n):
    if n < 2:
       return 1
    else:
        return n * factorial(n-1)

print(f'El factorial de {num} = {factorial(num)}')


'''
Ejemplo de Succesión de Fibonacci
'''

def fib(n):
    '''
    funcion que devuelve el numero de Fibonacci dado su orden
    Para más información acerca de esta función se puede consultar
    en: https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

resultado = [fib(0), fib(1), fib(2), fib(3), fib(4), fib(5), 
             fib(6), fib(7), fib(8), fib(9), fib(10)]

print(resultado)
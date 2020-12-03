Para este ejercicio so introduciré dos conceptos en matemáticas muy conocidos, que nos permitirán ver dos ejemplos de las funciones recursivas.

**Sucesión de Fibonacci**: a sucesión comienza con los números 0 y 1,​ a partir de estos, cada término es la suma de los dos anteriores, es la relación de recurrencia que la define. Para más información podéis consultar en este [enlace](https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci).

Por ejemplo la serie sería: 0, 1, 3, 5, 8, 13, 21, 34...

Para realizar una función que nos devuleva la sucesión de Fibonacci tenemos que crear una función recursiva.

Primero limitaremos la función a un numero de entrada que será la posición que queremos, también se suele llamar orden. Como el hay dos casos particulares que son el caso del cero y del uno estos se tienen que ser tratados independientemente en el que el caso del 0 tenemos que devolver un cero y en caso de uno tiene que devolver este mismo. A partir de aquí lo podemos hacer es devolver la suma del valor anterior y dos anteriores, volviendo a llamar la misma funcion y de esta forma llamamos recursivamente hasta que llega al final.

Aquí tenéis el código para la serie de Fibonacci:
```
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
```

Pero con esto solo nos devolverá un numero, así que si queremos solo tenemos que pedirle la succession manualmente, más adelante conoceremos métodos para realizar esto de forma más simple.

```
>>> [fib(0), fib(1), fib(2), fib(3), fib(4), fib(5), fib(6), fib(7), fib(8), fib(9), fib(10)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

**Factorial**: El factorial de un entero positivo n, el factorial de n o n factorial se define en principio como el producto de todos los números enteros positivos desde 1 (es decir, enteros) hasta n. Para más información podéis consultar en este [enlace](https://es.wikipedia.org/wiki/Factorial).

Por ejemplo el factorial de 4! = 1 x 2 x 3 x 4 = 24

Ahora que habéis visto el ejemplo de una función recursiva en este ejercicio debéis realizar la función de factorial. Podéis probar con el valor 4 que tenéis el resultado y así comprobar que está bien.

Como pista pensad que multiplicar por 1 es lo mismo que no hacer nada, así que cuando el valor sea uno o inferior ya ha acabado de calcular el valor.

Adjunto comprimido tenéis el ejemplo de la serie de Fibonacci.

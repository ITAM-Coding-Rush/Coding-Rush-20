# Descripción

Se dice que dos números enteros positivos $A$ y $B$ son amigos si la suma de los divisores propios de $A$ es igual a $B$ y la suma de los divisores propios de $B$ es igual a $A$.

Los divisores propios de un número $n$ son todos aquellos enteros positivos que dividen a $n$, pero sin incluir a $n$. Por ejemplo, los divisores propios de 12 son 1, 2, 3, 4 y 6.

Tu tarea es diseñar un código que diga si dos números son amigos o no.

# Entrada

En la primera línea, el entero $A$.

En la segunda línea, el entero $B$.

# Salida

Deberás imprimir "Son amigos" (sin comillas) si los enteros $A$ y $B$ son amigos, o "No son amigos" en otro caso.

# Ejemplo

||examplefile
sample
||description
Los divisores propios de 220 son: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110. La suma de estos es 284.

Los divisores propios de 284 son: 1, 2, 4, 71 y 142. La suma de estos es 220.

Por lo tanto, 220 y 284 son amigos.
||examplefile
sample2
||end

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>

Un ejemplo de números amigos son los números 220 y 284.

Crea un código que lea dos números A y B y diga si son amigos o no.

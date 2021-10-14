# Descripción
A Carlos y a sus amigos les encanta armar rompecabezas. Ellos están muy emocionados porque acaba de salir uno nuevo del hombre araña, el super héroe favorito de todos. Carlos les llevaba un rompecabezas a cada uno de sus amigos, pero se tropezó. ¡Ahora las piezas de todos los rompecabezas se mezclaron! Como estaban por entrar a la sesión del Coding Rush, no tuvieron más remedio que recoger las piezas que pudieran y empezar la clase. Lo bueno es que cada pieza venía marcada con un número del $1$ al $n$. Ayuda a Carlos a saber si puede armar un rompecabezas completo de las piezas que le quedaron. 

# Entrada
En la primera línea un entero positivo $n$, el número de piezas del rompecabezas. 
En la segunda línea un entero positivo $m$, el número de piezas que le quedaron a Carlos.
Después m líneas, cada línea con un número entre $1$ y $n$, indicando el número de pieza. 

# Salida
Imprime “WUUU” si Carlos tiene el rompecabezas completo, es decir, tiene al menos una copia de cada una de las $n$ piezas. 
Imprime “chale” si le falta al menos una pieza. 

# Ejemplo
||examplefile
sample1
||description
Entre las 5 piezas que se quedó, Carlos tiene cada una de las 3 piezas del rompecabezas. 
||examplefile
sample2
||description
Entre las 5 piezas que se quedó, Carlos solo logró tener la 1 y la 2. Como le falta la 3, se imprime "chale".
||end

# Límites

* $1<= n <= 1000 $
* $1<= m <= 1000 $

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>


# Descripción

Lorena es una alumna que le hacer rápido sus tareas. Actualmente cursa la materia de Circuitos Lógicos y recientemente vieron el tema de conversiones entre binario y decimal.

Ella sabe perfectamente como hacer el procedimiento a mano, pero siente que sería mejor si tuviera una aplicación que le ayude a hacer esa conversión. Como no tiene mucho tiempo libre te pide que le ayudes a hacer el programa que realice la conversión de binario a decimal.

**Explicación**

Para convertir de binario a decimal usaremos un ejemplo. Convertiremos $1010$ a un número decimal. Para ello, haremos una tabla como la siguiente:

| $2^3$ | $2^2$ | $2^1$ | $2^0$ |
| ----- | ----- | ----- | ----- |
| $1$   | $0$   | $1$   | $0$   |

_NOTA 1: Siempre debes hacer la tabla de derecha a izquierda y comenzando siempre con $2^0$._

_NOTA 2: En caso de que sea un número más grande necesitarás más columnas._

Ahora simplemente sumamos todas las columnas donde hay el valor '$1$'. En este caso sérá:

$2^3+2^1=8+2=10$

Por lo tanto, el número binario $1010$ es igual al número decimal $10$.

# Entrada

En la primera línea, un número $n$ que indica la cantidad de números binarios a convertir.
En las siguientes $n$ líneas vendrán los números en binario (léelos como cadena de texto).

# Salida

Deberás imprimir $n$ líneas con los números convertidos a decimal.

# Ejemplo

||examplefile
sample1
||examplefile
sample2
||end

# Descripción

Una profesora guarda para cada alumno el promedio de los $n$ exámenes que les ha aplicado. Decide no guardar ninguna otra información para no saturar la memoria de su computadora.

La profesora acaba de aplicar un examen adicional a los estudiantes y debe reportar el promedio final de cada uno de ellos. Al final ella reportará también a administración el promedio grupal.

Tu tarea es escribir un programa que le ayude a la profesora a calcular los estadísticos que debe reportar.

# Entrada

En la primera línea vendrá el entero $n$, el número de exámenes aplicados previamente.

En la segunda línea vendrá un entero $m$, que representa el número de alumnos en la clase.

Luego, para cada alumno de los $m$ alumnos recibirás su promedio actual (antes del nuevo examen) y la calificación que obtuvo en el examen nuevo.

# Salida

Para cada estudiante imprime el promedio final que obtuvo (contando el examen nuevo).

Finalmente, imprime el promedio final grupal, el promedio más alto y el más bajo.

**Nota**: Cada número impreso deberá estar redondeado a 3 cifras decimales. Para redondear un número $x$ a tres decimales puedes usar la función `round(x, 3)`.

# Ejemplo

||examplefile
sample
||description
En este ejemplo el grupo cuenta con 2 estudiantes, y se han realizado previamente 2 examenes. 

El primer estudiante tiene un promedio de 8 y una calificación en el tercer examen de 9.5. Por lo que su promedio final es de 8.5.

El segundo estudiante tiene un promedio de 9.1 y una calificación en el tercer examen de 9.7. Por lo que su promedio final es de 9.3

Al final, el promedio grupal es de 8.9.
||end

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>
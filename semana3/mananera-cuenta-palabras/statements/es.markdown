# LA MAÑANERA (CUENTA PALABRAS)


# Descripción

Una empresa de Análisis y Marketing Político tiene como objetivo conocer cuál es la palabra que más utiliza el presidente Andrés Manuel López Obrador en sus discursos de la mañanera para determinar si sus expresiones tienen patrones con algún sesgo ideológico y político negativo.

Para lograr dicho objetivo, la empresa te ha pedido que los ayudes a desarrollar un programa que cuente las palabras de N discrusos y devuelva la palabra más repetida con la cantidad de veces que las repitió.


# Entrada

Primero, leerás un número $N$ que representa la cantidad de discrusos a analizar. 

Después, leerás la lista de N discrusos. $Cada discurso estará en una línea distinta, en minúsculas y sin puntuación$.

Puedes asumir que siempre habrá al menos $N$ = 1 como entrada de la cantidad de discursos y siempre habrá una palabra más repetida que todas las demás.


# Salida

En la primera línea, la $palabra más repetida$ y, en la segunda línea, la $cantidad de veces$ que fue repetida esa palabra.




# Ejemplo

| Entrada                       | Salida    | Descripción |
|--------------                 |-----------|-------------|
| 5                             | 4         |             |
| me canso ganso                | me        |             |
| me colmaron el plato          |           |             |
| al margen de la ley nada      |           |             |
| por encima de la ley nadie    |           |             |
| todos me protegen y me cuidan |           |             |


<details>
<summary>Checa la `plantilla.py`</summary>
{{plantilla.py}}
</details>
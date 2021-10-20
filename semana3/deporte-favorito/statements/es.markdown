# **Deporte favorito**

El equipo de Coding Rush se encontraban platicando sobre las Olimpiadas afuera de las salas de cómputo. Cada voluntario comienza a hablar de su equipo favorito. El equipo quiere saber cuál es el deporte más popular entre los voluntarios del Coding Rush. Tú les propones crear un programa que cuente los votos y muestre cuál es el deporte más popular.

# **Explicación**
Deberás utilizar un diccionario que contenga los siguientes deportes:
* futbol
* basquetball
* volleybol
* atletismo
* handball
* otros

# **Entrada**
* Un número $n$ que indica la cantidad de votos a introducir.
* $n$ líneas con los votos de todos los deportes.
  * Para cada voto debes escribir la inicial del deporte (consulta los ejemplos). Si la letra no coincide con ningún deporte, el voto va para *otros*.

# **Salida**
* El nombre del deporte con más votos.
* El número de votos de ese deporte.

# **Ejemplo**
||input
6
f
f
f
f
h
h
||output
futbol
4
||input
7
k
a
r
h
a
p
h
||output
otros
3

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>
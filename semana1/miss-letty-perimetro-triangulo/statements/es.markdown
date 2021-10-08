# MISS LETTY (PERÍMETRO DE TRIÁNGULOS)

# Descripción

Para que sus alumnos no se copien en el examen de geometría, Miss Letty decidió dar diferentes coordenadas de vértices del triángulo a cada alumno.
Sin embargo, esta cruel estrategia le salió contraproducente porque ahora tiene que calcular el perímetro de todos esos triángulos.

Para evitar hacer tantas cuentas y poder ver su serie de Netflix favorita, Miss Letty ha pedido tu ayuda para crear un programa que reciba tres pares de coordenadas que representan los vértices de un triángulo y calcule su perímetro.

Recuerda que la distancia de dos puntos sobre un plano de dos dimensiones está definida como:
$$d={ \sqrt{(x2-x1)^2 + (y2-y1)^2}}$$

Recuerda cómo elevar un número a alguna potencia usando Python y recuerda que sacar la raíz cuadrada de algún número es equivalente a elevarlo a la 1/2 que es igual 0.5.
$$d={ ( (x2-x1)^2 + (y2-y1)^2 ) )^\frac{1}{2} } ={ ( (x2-x1)^2 + (y2-y1)^2 ) )^\frac{0.5}{} }$$

# Entrada

Leerás la lista de 3 pares ordenados, es decir, leerás 6 números reales (floats), uno por cada línea.

El número leído en la primera línea será x1, en la segunda línea será y1, en la tercera línea será x2, en la cuarta línea será y2, en la quinta línea será x3 y, finalmente, en la sexta línea será y3.

# Salida

El número real correspondiente al perímetro del triángulo calculado redondeado a 3 decimales.

# Ejemplo

| Entrada | Salida | Descripción |
| ------- | ------ | ----------- |
| 2.2     | 16.332 |             |
| 1.0     |        |             |
| 4.5     |        |             |
| 4.5     |        |             |
| 8.8     |        |             |
| 1.0     |        |             |

<details>
<summary>Revisa la `plantilla.py`</summary>
{{plantilla.py}}
</details>

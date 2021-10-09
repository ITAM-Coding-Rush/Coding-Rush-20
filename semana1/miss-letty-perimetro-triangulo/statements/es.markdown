# Descripción

Para que sus alumnos no se copien en el examen de geometría, Miss Letty decidió dar diferentes coordenadas de vértices del triángulo a cada alumno.
Sin embargo, esta cruel estrategia le salió contraproducente porque ahora tiene que calcular el perímetro de todos esos triángulos.

Para evitar hacer tantas cuentas y poder ver su serie de Netflix favorita, Miss Letty ha pedido tu ayuda para crear un programa que reciba tres pares de coordenadas que representan los vértices de un triángulo y calcular su perímetro.

Recuerda que la distancia de dos puntos sobre un plano de dos dimensiones está definida como:

$$d={ \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}}$$

Recuerda cómo elevar un número a alguna potencia usando Python y recuerda que sacar la raíz cuadrada de algún número es equivalente a elevarlo a la 1/2 (que es igual 0.5).

$$d = { ( (x_2-x_1)^2 + (y_2-y_1)^2 ) ^\frac{1}{2} } = { ( (x_2-x_1)^2 + (y_2-y_1)^2 ) ^{0.5} }$$

# Entrada

Leerás la lista de 3 puntos en el plano; es decir, leerás 6 números reales (floats), uno por cada línea.

El número leído en la primera línea será $x_1$, en la segunda línea será $y_1$, en la tercera línea será $x_2$, en la cuarta línea será $y_2$, en la quinta línea será $x_3$ y, finalmente, en la sexta línea será $y_3$.

# Salida

El número real correspondiente al perímetro del triángulo calculado redondeado a 3 decimales.

**Nota**: Para redondear un número $x$ a tres decimales puedes usar la función `round(x, 3)`.

# Ejemplo

||examplefile
sample
||end

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>

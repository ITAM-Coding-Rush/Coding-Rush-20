# NUMEROLOGÍA

# Descripción

Diego está harto de que Xime quiera predecir su futuro a través de la numerología.
En ocasiones, Xime le explica a Diego que su enojo es debido a Mercurio Retrograda y Diego ya no lo soporta.
Es por eso que, como buen escéptico e ingeniero, Diego ha decidido comprobar si la numerología tienes sentido a través de un experimento estadísitco.

Para llevar a cabo su experimento, Diego le va a preguntar a Xime qué significado tienen los números pares e impares en la Numerología, va a calcular la Carta Numerológica de cada participante y va a imprimir una lista del significado de la Carta Numerológica de cada uno para, posteriormente, confirmar con cada participante si tiene sentido.

Para calcular la Carta Numerológica, de manera simplificada y para fines prácticos de este ejercicio, se deben sumar todos los dígitos de la fecha de nacimiento hasta que quede un solo dígito.
Es decir, mientras el resultado de la suma no sea un sólo dígito (0,1,2,3,4,5,6,7,8,9), se tienen que sumar, otra vez, todos los dígitos de esa suma.

Por ejemplo, si la fecha de nacimiento de Diego es 15/06/1998:
Primero, sumo los dígitos de mi fecha de nacimiento: 1 + 5 + 0 + 6 + 1 + 9 + 9 + 8 = 39
Como la suma resultante aún no tiene 1 sólo dígito, vuelvo a sumar cada uno de sus dígitos: 3 + 9 = 12
Como la suma resultante aún no tiene 1 sólo dígito, vuelvo a sumar cada uno de sus dígitos: 1 + 2 = 3
Finalmente, como la suma es un sólo dígito, he terminado y encontrado el número de mi Carta Numerológica.

Si el número resultante es un número PAR, se dice que la persona es muy "ESTÁTICA"; mientras que si es IMPAR, se dice que la persona es muy "DINÁMICA".

Con el ejemplo anterior, es evidente que Diego es una persona muy "DINÁMICA".

Como a Diego le da flojera calcular la Carta Numerológica de cada participante,
te ha pedido que lo ayudes a desarrollar un programa que lo haga de manera automatizada.

# Entrada

Primero, leerás un número $N$ que representa la cantidad de participantes en el experimento.

Después, leerás la lista de $N fechas de nacimiento$. Cada fecha de nacimiento de seis dígitos
estará escrita en una misma línea y sin espacios. ($Ej. 15061998$)

# Salida

La lista con las $N sumas y respuestas$ para cada participante: $"ESTÁTICA"$ si la suma fue par ó $"DINÁMICA"$ si la suma fue impar.
(Las respuestas deben estar en mayúsculas y con acento. No olvides que la ortografía es importante.)

En una línea se debe imprimir la suma y, en la siguiente línea, se debe imprimir la respuesta.

# Ejemplo

| Entrada  | Salida   | Descripción |
| -------- | -------- | ----------- |
| 3        | 3        |             |
| 14061990 | DINÁMICA |             |
| 01112001 | 6        |             |
| 24121995 | ESTÁTICA |             |
|          | 6        |             |
|          | ESTÁTICA |             |

<details>
<summary>Revisa la `plantilla.py`</summary>
{{plantilla.py}}
</details>

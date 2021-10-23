# Descripción

En la epoca de los dinosaurios la comunicación que estos tenían era un poco más sencilla que la que nosotros pensamos. Realmente los dinosaurios solo podían decir una palabra: Rawr (Un rugido). El significado de cada rugido cambiaba según cuánto durara, es decir, la cantidad de 'a's que tuviera. O como diría Dinosé José Raawr y Raaaaawr no es igual Raawr es sufrir y Raaaaawr es gozar.

Existen dinosaurios a los que les cuesta trabajo distinguir los sonidos entre los distintos rugidos, y otros dinosaurios los molestan usando rugidos sin sentido o que no conocen. Por este motivo tus dino amigos te han pedido que les escribas un codigo que les permita entender lo que los otros dinosaurios les quieren decir o saber si solo los están molestando.

Por favor ayúdalos, porque si no se logran comunicar se van a extinguir :(

# Entrada

Un número $N$ que representa la cantidad de palabras que el dinosaurio conoce

$N$ pares de datos que representan el rugido y su significado de la siguiente manera:

- Un número $M$ que representa la cantidad de A's en el rugido
- El significado del rugido

Un número $K$ que representa la cantidad de rugidos a traducir

$K$ rugidos

# Salida

$K$ palabras que representan la traducción de los rugidos.

En caso de que la palabra no este en el diccionario de traducciones debes imprimir 'Solo te esta molestando' indicando que es un rugido sin sentido

# Ejemplo

||examplefile
sample
||description

- 'raawr' tiene 2 'a's en el rugido, lo que significa 'amar'.
- 'raaaaawr' tiene 5 'a's en el rugido, lo que significa 'querer'.
- 'raaaaaaaaaaaaaawr' tiene 14 'a's en el rugido, lo que no es una palabra que conozcas, por lo tanto solo están molestando.

||end

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>

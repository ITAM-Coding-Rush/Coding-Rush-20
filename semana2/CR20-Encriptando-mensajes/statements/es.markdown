# Descripción

Tus amigos Limón y Lorena están llevando juntos la clase de Bases de Datos con el famosísimo profesor Floppy. Como sun muy aplicados, hicieron la promesa de no distraerse durante la clase, por lo que las únicas herramientas que usarán en clase son _Oracle SQL Developer_ y _zoom_. Durante la clase solo se podrán comunicar vía _zoom_, pero no quieren que Floppy se entere de qué están hablando. Así que investigando un poco descrubrieron la encriptación César.

La encriptación César consiste en que las letras de la frase original serán cambiadas por las letras recorridas una **X** cantidad de posiciones. Por ejemplo, la frase "hola mundo", en encriptación César, con x = 3 pasaría a ser "krod pxqgr".

Lorena decidió ocupar el número 5, para recorrer 5 letreas su frase y Limón decidió ocupar el número 6 para recorrer su frase. Como ambos son muy estudiosos no tienen tiempo para hacer un programa que los ayude a encriptar los mensajes, por lo que te han pedido que les ayudes a crear un programa para encriptar sus mensajes. Ellos te indicarán la cantidad de mensajes a encriptar, de quién es el mensaje y por último, el mensaje a encriptar. Lorena Se identificara con _lo_ y Limón con _li_.

# Entrada

Un numero $N$ que indica la cantidad de frases a encriptar $N$ pares de líneas. La primera línea indica si el mensaje a encriptar es de Limon o de Lorena ( _li_ o _lo_). La segunda línea indica el mensaje a encriptar, te aseguramos que todos los mensajes estarán en minúsculas y no tendrán ningún tipo de signos de puntuación.

# Salida

Cada una de las frases encriptadas, es decir, N frases encriptadas.

# Ejemplo

||examplefile
sample1
||end

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>

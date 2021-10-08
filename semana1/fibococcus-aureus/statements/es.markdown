# Descripción

Recientemente un grupo de científicos ha descubierto una nueva bacteria, la han llamado “Fibococcus aureus”. Javier, quien lidera la investigación ha observado que la bacteria tiene un crecimiento muy peculiar: 

 - Una bacteria puede dividirse en ella misma y un hijo si han pasado 2 o más minutos desde su nacimiento.
 - Se garantiza que después esos 2 minutos, la bacteria SIEMPRE se dividirá por cada minuto que pase.
 - Al parecer la vida de esta bacteria es de 1 año, por lo que no hay que preocuparse de su muerte.  

Javier sabe que tú eres un programador muy habilidoso y te ha pedido que le ayudes a determinar la cantidad de bacterias que habrá después de una n cantidad de minutos.

# Entrada

Un número entero 0<=n<=100 que representa la cantidad de minutos que han pasado desde el nacimiento de la primer bacteria hasta la última. 

# Salida

La cantidad de bacterias que habrá después de los n minutos. 

# Ejemplo

||examplefile
sample1
||description
Se presupone que la bacteria que Javier observará acaba de nacer.
||end

||examplefile
sample2
||description
En el minuto 1 la bacteria1 aún no es capaz de dividirse, por lo que solamente hay 1 bacteria.
||end

||examplefile
sample3
||description
En el minuto 2 la bacteria1 puede dividirse y tiene un hijo.
||end

||examplefile
sample4
||description
En el minuto 3 la bacteria1 tiene un nuevo hijo y la bacteria2 aún no puede dividirse.
||end

||examplefile
sample5
||description
En el minuto 4 la bacteria1 tiene un nuevo hijo, la bacteria2 tiene su primer hijo y la bacteria3 aún no puede dividirse.
||end

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>
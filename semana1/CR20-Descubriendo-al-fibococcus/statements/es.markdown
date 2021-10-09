# Descripción

Recientemente un grupo de científicos ha descubierto una nueva bacteria, la han llamado “Fibococcus aureus”. Javier, quien lidera la investigación ha observado que la bacteria tiene un crecimiento muy peculiar:

- A partir de los dos minutos de su nacimiento, la bacteria SIEMPRE genera un nuevo hijo por cada minuto que pasa.
- Antes de los dos minutos, no genera ningún hijo.
- Al parecer, la vida de la bacteria es muy prolongada, por lo que no hay que preocuparse de su muerte.

Javier sabe que tú eres un programador muy habilidoso y te ha pedido que le ayudes a determinar la cantidad de bacterias que habrá después de una $n$ cantidad de minutos.

# Entrada

Un número entero $n$ que representa la cantidad de minutos que han pasado desde el nacimiento de la primer bacteria hasta la última.

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

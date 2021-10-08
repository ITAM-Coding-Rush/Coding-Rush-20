#Solución: Numerología

#Leer cantidad de participantes
n = int(input())

#Inicializar lista para ir anexando las respuestas de cada iteración
resp = []

#Iterar por cada fecha leída
for i in range(n):
    
    #Inicializar suma y leer fecha 
    sum = 0
    fecha = input()
    
    #Iterar fecha para sumar dígitos
    for char in fecha:
        sum = sum + int(char)
    
    #Mientras la suma siga siendo mayor a 9, iterar suma y sumar digitos
    while(sum > 9):
        str_sum = str(sum)
        sum = 0
        for digit in str_sum:
            sum = sum + int(digit)
    
    #Anexar resultado de la suma al arreglo de respuesta
    resp.append( str(sum) )

    #Anexar respuesta al arreglo dependiendo si es par o impar
    if( sum % 2 == 0):
        resp.append("ESTÁTICA")
    else:
        resp.append("DINÁMICA")

#Imprimir respuestas
for element in resp:
    print(element)

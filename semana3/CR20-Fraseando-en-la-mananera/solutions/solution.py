#Solución: La Mañanera (Cuenta Palabras)

#Leer cantidad (N) de líneas/discrusos a analizar
n = int(input())

#Inicializar diccionario
dic = {}

#Iterar para leer N líneas
for i in range(n):
    #Leer línea/discruso
    str_discurso = input()
    arr_discurso = str_discurso.split()

    #Iterar discurso
    for palabra in arr_discurso:
        #Contar cada palabra
        if(palabra in dic):
            dic[palabra] = dic[palabra] + 1
        else:
            dic[palabra] = 1
    
#Iterar diccionario para obtener palabra más repetida
cant_max = 0
palabra_max = ""

for key in dic:
    if( dic[key] > cant_max ):
        cant_max = dic[key]
        palabra_max = key

print(palabra_max)
print( str(dic[palabra_max]) )
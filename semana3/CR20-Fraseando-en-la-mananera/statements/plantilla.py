#PLANTILLA


#Leer cantidad N de líneas/discrusos a analizar
n = #???

#Inicializar diccionario
dic = #???

#Iterar para leer N líneas
for i in range(n):
    #Leer línea/discruso y convertir en array
    str_discurso = #???
    arr_discurso = str_discurso.split()

    #Iterar discurso
    for palabra in #???:
        #Contar cada palabra
        if(palabra in dic):
            dic[palabra] = #???
        else:
            dic[palabra] = #???
    
#Iterar diccionario para obtener palabra más repetida
cant_max = 0
palabra_max = ""

for key in #???:
    if( dic[key] > cant_max ):
        #???
        #???

print(#???)
print(#???)
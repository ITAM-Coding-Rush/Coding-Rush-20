#leemos n
n = int(input())

#leemos m
m = int(input())

#guardamos las piezas en un arreglo
piezas = [0]*(n+1)
for i in range(m):
    piezas[i] = int(input())

#para cada pieza checamos si esta entre las que tenemos
resp = "WUU"
for i in range(1, n+1):
    esta = False
    for j in range(m):
        if piezas[j] == 1:
            esta = True
    #si no esta, cambiamos la respuesta
    if esta == False:
        resp = "chale"

#imprimimos la respuesta
print(resp)
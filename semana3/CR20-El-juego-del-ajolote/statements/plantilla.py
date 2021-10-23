# Leemos el número de voluntarios
n = int(input())

# Diccionarios para calcular la respuesta
puntos_por_equipo = {}
puntos_por_voluntario = {}
equipo_voluntario = {}

for i in range(n):
    # Lemos los datos del voluntario
    nombre = input()
    equipo = input()
    atrapados = int(input())
    # Guardamos el equipo del voluntario
    equipo_voluntario[] =
    # Guardamos los puntos del voluntario
    puntos_por_voluntario[] =
    # Acutalizamos los puntos del equipo del voluntario
    if  not in :
        puntos_por_equipo[ ] = 
    puntos_por_equipo[] = 

# Buscamos el equipo ganador
equipo_ganador = ""
puntos_equipo = -1

for  in :
    if :
        puntos_equipo = 
        equipo_ganador = 

print(equipo_ganador)

# Buscamos al voluntario que hizo
# más reportes dentro del equipo ganador
voluntario_ganador = ""
puntos_voluntario = -1

for  in :
    # Recordar que el voluntario debe ser del equipo ganador
    if   and :
        puntos_voluntario = 
        voluntario_ganador = 

print(voluntario_ganador)

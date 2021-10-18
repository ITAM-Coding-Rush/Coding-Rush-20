n = int(input())

puntos_por_equipo = {}
puntos_por_voluntario = {}
equipo_voluntario = {}

for i in range(n):
    nombre = input()
    equipo = input()
    atrapados = int(input())

    equipo_voluntario[nombre] = equipo

    if equipo not in puntos_por_equipo:
        puntos_por_equipo[equipo] = 0
    puntos_por_equipo[equipo] += atrapados

    puntos_por_voluntario[nombre] = atrapados

# Buscamos el equipo ganador
equipo_ganador = ""
puntos_equipo = -1

for k in puntos_por_equipo:
    if puntos_por_equipo[k] > puntos_equipo:
        puntos_equipo = puntos_por_equipo[k]
        equipo_ganador = k

print(equipo_ganador)

# Buscamos al voluntario que hizo
# más reportes dentro del equipo ganador
voluntario_ganador = ""
puntos_voluntario = -1

for k in puntos_por_voluntario:
    if puntos_por_voluntario[k] > puntos_voluntario and equipo_voluntario[k] == equipo_ganador:
        puntos_voluntario = puntos_por_voluntario[k]
        voluntario_ganador = k

print(voluntario_ganador)

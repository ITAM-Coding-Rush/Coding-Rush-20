# Pide los n votos.
n = int(input())

# Inicialización del diccionario que contiene los deportes:
# futbol, baloncesto, voleibol, atletismo, handball.
deportes = {'futbol': 0, 'baloncesto': 0, 'voleibol': 0,
            'atletismo': 0, 'handball': 0, 'otros': 0}

for i in range(n):
  # Lectura de votos
  votos = input()

  # Aumentamos los contadores.
  if votos == 'f':
    deportes['futbol'] += 1
  elif votos == 'b':
    deportes['baloncesto'] += 1
  elif votos == 'v':
    deportes['voleibol'] += 1
  elif votos == 'a':
    deportes['atletismo'] += 1
  elif votos == 'h':
    deportes['handball'] += 1
  else:
    deportes['otros'] += 1

# La variable maximo guarda la llave del deporte con más votos.
maximo = max(deportes, key = deportes.get)

# Imprime el nombre del deporte.
print(maximo)
# Imprime el número de votos.
print(deportes[maximo])

# Leemos la cantidad de números a convertir
n = int(input())

for i in range(n):
    # Leemos el número a convertir
    binario = input()
    # Guardamos en una variable la respuesta
    decimal = 0
    # Iteramos sobre el número
    for i in range(1, len(binario)+1):
        if binario[-i] == "1":
            # ¿Cuánto debemos sumar a la respuesta si está el i bit prendido?
            decimal += 2 ** i
    print(decimal)

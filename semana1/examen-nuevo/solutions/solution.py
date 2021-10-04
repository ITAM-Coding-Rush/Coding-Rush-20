N = int(input())
A = int(input())

grupal = 0.0

for i in range(A):
    calificacion = float(input())
    nuevo = float(input())
    actualizado = ((calificacion*N)+nuevo)/(N+1)
    grupal += actualizado
    print(round(actualizado, 3))

grupal /= A
print(round(grupal, 3))

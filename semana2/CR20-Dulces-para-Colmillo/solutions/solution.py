n = int(input())
dulces = [0]*n

for i in range(n):
    dulces[i]= input()

m = int(input())

for i in range(m):
    categoria = input()
    if categoria in dulces:
        print("Colmillo feliz")
        aux=dulces.count(categoria)
        print(dulces.count(categoria))
    else:
        print("Colmillo triste")
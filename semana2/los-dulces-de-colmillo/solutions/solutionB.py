dulces = {
    "Caramelos": 0,
    "Chocolates": 0,
    "Bombones": 0,
    "Paletas": 0,
    "Golosinas": 0
}

n = int(input())
for i in range(n):
    dulces[input()] += 1

m = int(input())
for i in range(m):
    p = input()
    cnt = dulces[p] if p in dulces else 0
    if cnt == 0:
        print("Colmillo triste")
    else:
        print("Colmillo feliz")
        print(cnt)

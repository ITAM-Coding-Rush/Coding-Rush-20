dic = {}
n = int(input())

for i in range(n):
    m=int(input())
    palabra=input()
    dic[m]=palabra

k = int(input())

for i in range(k):
    rugido = input()
    contadorA=0
    for c in rugido:
        if c=='a':
            contadorA+=1
    if contadorA in dic:
        print(dic[contadorA])
    else:
        print('Solo te esta molestando')
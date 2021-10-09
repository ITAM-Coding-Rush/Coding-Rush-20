n = int(input())
m = int(input())

promedios = []
for _ in range(m):
    p = float(input())
    c = float(input())
    promedios += [(p * n + c) / (n + 1.0)]

for p in promedios:
    print(round(p, 3))

print(round(sum(promedios) / m, 3))
n = int(input())
for i in range(n):
    m = input()
    while len(m) > 1:
        m = str(sum([int(d) for d in m]))
    print(m)
    if int(m) & 1 == 0:
        print("ESTÁTICA")
    else:
        print("DINÁMICA")

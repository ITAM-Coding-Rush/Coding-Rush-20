c1 = int(input())
p1 = int(input())
c2 = int(input())
p2 = int(input())
efectivo = int(input())

total = c1*p1 + c2*p2

if total <= efectivo:
    print("Le alcanza")
else:
    print(total-efectivo)
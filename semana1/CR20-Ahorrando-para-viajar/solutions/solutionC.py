Dolar = 20.51
CT = 300

pesosNeeded = CT * Dolar
p = int(input())

print(p / Dolar)

if pesosNeeded <= p:
    print("Fondos suficientes")
else:
    print("Fondos insuficientes")

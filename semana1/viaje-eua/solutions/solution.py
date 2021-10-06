Dolar = 20.51
CT = 300
p = int(input())
d = p / Dolar
print(d) # El redondeo no afecta, es solo para un pretty print

if (d < CT):
    print("Fondos insuficientes")
else:
    print("Fondos suficientes")

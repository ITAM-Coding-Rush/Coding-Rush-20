A = int(input())
B = int(input())
C = int(input())
D = int(input())

numerador = A*D+B*C
denominador = B*D

if numerador % denominador == 0:
    print(numerador // denominador)
else:
    print(numerador)
    print(denominador)
    

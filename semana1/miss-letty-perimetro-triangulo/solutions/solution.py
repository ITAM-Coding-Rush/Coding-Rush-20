#Solución: Miss Letty (Perímetro de Triángulo)

#Leer pares ordenados
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

#Calcular distancias por lados
l1 =  ( (x2-x1)**2 + (y2-y1)**2 )**0.5
l2 =  ( (x3-x2)**2 + (y3-y2)**2 )**0.5
l3 =  ( (x3-x1)**2 + (y3-y1)**2 )**0.5

#Sumar la distancia de los tres lados 
perimetro = l1 + l2 + l3

#Redondear resultado a 3 decimales
perimetro = round(perimetro, 3)

#Imprimr resultado
print( str(perimetro) )

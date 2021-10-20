#leemos la oracion 
oracion = input()

#creamos un string que contenga las letras de la oracion, pero sin espacios
s = ""
for c in oracion:
  if c != " ":
    s += c
#ahora checamos si este string es un palindromo
esPalindromo = True
for i in range(len(s)):
  if s[i] != s[len(s)-1-i]:
    esPalindromo = False
#se imprime la respuesta
if esPalindromo: 
  print("PALINDROMA!")
else: 
  print("Intenta con otra")
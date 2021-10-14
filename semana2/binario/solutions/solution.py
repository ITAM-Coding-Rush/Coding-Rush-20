n = int(input())

for i in range(n):
  cont = 0
  decimal = 0
  binario = input();
  for num in binario[::-1]:
    if num == "1":
      decimal += 2 ** cont
    cont += 1
  print(decimal)
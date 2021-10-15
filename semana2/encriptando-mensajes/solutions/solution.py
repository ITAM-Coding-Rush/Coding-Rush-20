n = int(input())

for i in range(n):
	persona = input()
	frase = input()

	nueva_frase = ""

	if persona == "lo":
		for c in frase:
			if  97 <= ord(c) <= 122:
				if ord(c) >= 118:
					nueva_frase += chr((ord(c) + 5) - 26)
				else:
					nueva_frase += chr(ord(c) + 5)
			else:
				nueva_frase += " "
		print(nueva_frase)
	elif persona == "li":
		for c in frase:
			if  97 <= ord(c) <= 122:
				if ord(c) >= 117:
					nueva_frase += chr((ord(c) + 6) - 26)
				else:
					nueva_frase += chr(ord(c) + 6)
			else:
				nueva_frase += " "
		print(nueva_frase)
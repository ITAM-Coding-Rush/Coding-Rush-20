import string
import random

cases = 10
for i in range(cases):
    n = random.randint(1, 100)
    cadena = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))
    file = open("cases/" + str(i+1)+".in", "w")
    file.write(cadena)
    file.close()

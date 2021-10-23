import random

cases = 10
for i in range(cases):
    n = random.randint(1, 30)
    r = random.randint(1,n)    
    file = open("cases/" + str(i+1)+".in", "w")
    file.write(str(n)+"\n")
    file.write(str(r)+"\n")
    file.close()

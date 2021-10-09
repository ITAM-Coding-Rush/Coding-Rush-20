import random
import os
import itertools as it
from math import *

baseString = """
{A}
{B}
""".strip(' \t\n\r')

cases = 10

def sumaDivPropios(n):
    c = 0
    for i in range(1, ceil(sqrt(n)) + 1):
        if n % i == 0:
            if i != n:
                c += i
            if i * i != n and i != 1:
                c += n // i
    return c

random.seed(4)
MAXN = 10001
amigo = [0] * MAXN

pares = [] # son amigos
impares = [] # no son amigos
for i in range(1, MAXN):
    amigo[i] = sumaDivPropios(i)

for i in range(1, MAXN):
    if i <= amigo[i] < MAXN and i == amigo[amigo[i]]:
        pares += [(i, amigo[i])]

random.shuffle(pares)

for i in range(cases):
    caseName = '{}.{}.in'.format(i // 2, i)

    if i % 2 == 0:
        A, B = pares[i//2]
    else:
        A = random.randint(1, 1000)
        B = random.randint(1, 1000)

    case = {
        'A': A,
        'B': B
    }

    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)

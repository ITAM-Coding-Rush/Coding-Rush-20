import random
import os
import itertools as it
from math import *

baseString = """
{n}
{alumnos}
""".strip(' \t\n\r')

random.seed(2)

cases = 10

for i in range(cases):
    caseName = '{}.in'.format(i)

    alumnos = []

    n = 0
    puntos = random.randint(1, 100)
    equipos = random.randint(1, 50 // (10-i))
    for i in range(equipos):
        e = []
        s = puntos
        while s > 0:
            aux = random.randint(0, s)
            s -= aux
            e += [aux]
        e.sort()
        if len(e) > 1 and e[-1] == e[-2]:
            e[-1] += 1
            e[-2] -= 1
        
        for ee in e:
            n += 1
            alumnos += ["a{}\ne{}\n{}".format(n, i+1, ee)]
        
    random.shuffle(alumnos)

    case = {
        'n': n,
        'alumnos': "\n".join(alumnos)
    }

    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)


    
    

    

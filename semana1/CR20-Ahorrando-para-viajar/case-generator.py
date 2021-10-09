import random
import os
import itertools as it
from math import *

baseString = """
{pesos}
""".strip(' \t\n\r')

cases = 10
pesos = [0, ceil(300*20.51), floor(300*20.51),
         round(100*20.51), round(200*20.51),
         round(400*20.51), round(500*20.51),
         1e9, 100, ceil(299*20.51)]

for i in range(cases):
    caseName = '{}.in'.format(i)

    case = {
        'pesos': int(pesos[i]),
    }

    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString + "\n")

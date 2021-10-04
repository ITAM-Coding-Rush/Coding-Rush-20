import random
import os
import itertools as it
from math import *

baseString = """
{n}
{m}
{calis}
""".strip(' \t\n\r')

cases = 10

for i in range(cases):
    caseName = '{}.in'.format(i)

    n = random.randint(1, 10**i)
    m = random.randint(1, 10**((i+1) // 3))

    calis = [str(random.randint(50, 100) / 10.0) for _ in range(2*m)]

    case = {
        'n': n,
        'm': m,
        'calis': "\n".join(calis)
    }

    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)

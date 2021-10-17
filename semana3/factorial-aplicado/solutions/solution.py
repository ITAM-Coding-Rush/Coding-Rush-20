
N=int(input())
R=int(input())

nFac=1
for i in range(N,1,-1):
    nFac*=i

rFac=1
for i in range(R,1,-1):
    rFac*=i

n_rFac=1
for i in range(N-R,1,-1):
    n_rFac*=i

nCr=int(nFac/(rFac*n_rFac))

print(nCr)
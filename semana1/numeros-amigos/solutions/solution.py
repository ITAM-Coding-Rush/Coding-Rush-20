A = int(input())
B = int(input())
sumdivpA = 0
sumdivpB = 0
for a in range(1, A):
    if A % a == 0:
        sumdivpA += a
for b in range(1, B):
    if B % b == 0:
        sumdivpB += b
if sumdivpA == B and sumdivpB == A:
    print("Son amigos")
else:
    print("No son amigos")

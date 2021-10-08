n = int(input())
a = 0
b = 1
c = 0
for k in range(n):
    c=a+b
    a=b
    b=c
print(c)
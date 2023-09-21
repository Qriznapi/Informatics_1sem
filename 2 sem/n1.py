b = list(map(int, input().split()))
a = b[0]
s = 0
for i in range(1, len(b)):
    s += b[i]
print(a*(a+1)//2 - s)
c = list(map(str, input().split()))
a = int(c[0])
b = c[1]
s = ""
for i in range(len(b) // a):
    for j in range(a):
        s += b[(i + 1) * a - j - 1]
print(s)
a = list(map(str, input().split()))
b = []
for i in a:
    if a.count(i) == 1:
        b.append(i)
print(*b)
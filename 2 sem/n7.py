n = 0
cnt = 0
a = list(map(str, input().split()))
for i in a:
    if a.count(i) > cnt:
        cnt = a.count(i)
        n = i
print(n)
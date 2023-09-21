n = int(input())
a = list(map(int, input().split()))
num = 0
for i in range(n):
    cnts = 0
    cntb = 0
    for j in range(n):
        if a[i] >= a[j]:
            cntb += 1
        if a[i] <= a[j]:
            cnts += 1
    if cnts > n // 2 and cntb > n // 2:
        num = a[i]
print(num)
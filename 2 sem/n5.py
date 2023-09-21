a = list(map(str, input().split()))
print(a[-1], *[a[i] for i in range(len(a) - 1)])

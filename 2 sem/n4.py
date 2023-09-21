a = list(map(str, input().split()))
print(*[a[i + pow(-1, i)] for i in range(len(a) - (len(a) % 2))], a[-1] if len(a) % 2 == 1 else '')

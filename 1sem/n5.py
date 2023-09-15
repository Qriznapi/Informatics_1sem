def to10(a, b):
    a = int(a)
    s = 0
    i = 0
    while a > 0:
        s += (a % 10) * (b ** i)
        i += 1
        a /= 10
        a = int(a)
    return (s)
def from10(a, b):
    i = 0
    s = 0
    while a > 0:
        s += 10**i * (a % b)
        i += 1
        a /= b
        a = int(a)
    return (s)
a, b, c = map(int, input().split())
print (from10(to10(a, b), c))
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
f = open('input.txt')
a = list(map(int, f.readline().split()))
b = list(map(str, f.readline().split()))
c = list(map(int, f.readline().split()))
for j in range(len(a)):
    a[j] = to10(a[j], c[0])
if (b[0] == "+"):
    s = 0
    for i in a:
        s += int(i)
    f = open('output.txt', 'w')
    f.write(str(from10(s, c[0])))
    f.close()
if (b[0] == "-"):
    s = 2 * a[0]
    for i in a:
        s -= i
    f = open('output.txt', 'w')
    f.write(str(from10(s, c[0])))
    f.close()
if (b[0] == "*"):
    s = 1
    for i in a:
        s *= i
    f = open('output.txt', 'w')
    f.write(str(from10(s, c[0])))
    f.close()
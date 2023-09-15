f = open('input.txt')
a = list(map(int,f.readline().split()))
b = f.readline()
if (b == "+"):
    s = 0
    for i in a:
        s += int(i)
    f = open('output.txt', 'w')
    f.write(str(s))
    f.close()
if (b == "-"):
    s = 2 * a[0]
    for i in range(len(a)):
        s -= a[i]
    f = open('output.txt', 'w')
    f.write(str(s))
    f.close()
if (b == "*"):
    s = 1
    for i in a:
        s *= i
    f = open('output.txt', 'w')
    f.write(str(s))
    f.close()
f = open('input10.txt')
b = list(map(str,f.read().split()))
glas = ['a', 'e', 'i', 'o', 'u', 'y']
a = []
for i in b:
    a.extend(i)
#a = f.read()
n = 0
for j in range(0, len(b)):
    y = ""
    for i in range(len(b[j])):
        if (b[j][i] in glas):
            if (i < len(b[j]) - 1):
                if (b[j][i + 1] not in glas):
                    y += b[j][i] + "c" + b[j][i]
                    print(i)
                    print(y, b[j], len(b[j]))
            else:
                y += b[j][i] + "c" + b[j][i]
                print(i)
                print(y, b[j], len(b[j]))
        else:
            y += b[j][i]
    b[j] = y
f = open('output10.txt', 'w')
#f.write(str(b))
f.write(str(b))
f.close()
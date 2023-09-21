#print(ord("9"))
f = open('input9.txt')
b = list(map(str,f.read().split()))
a = []
for i in b:
    a.extend(i)
#a = f.read()
n = 0
for i in range(1, len(a)):
    if (a[i] == '!' or a[i] == '?' or a[i] == '.' or a[i] == ';'):
        if (ord(a[i - 1]) >= 65 and ord(a[i - 1]) <= 90) or (ord(a[i - 1]) >= 97 and ord(a[i - 1]) <= 122):
            n += 1
#65 90
#97 122
#48 57
f = open('output9.txt', 'w')
#f.write(str(b))
f.write(str(n))
f.close()
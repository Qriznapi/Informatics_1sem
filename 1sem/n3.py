a = list(map(int, input().split()))
s = 1
for i in a:
    s *= i
print (pow(s, 1/len(a)))
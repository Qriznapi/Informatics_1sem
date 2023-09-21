b = ['A', 'H', 'I', 'M', 'O', 'T,' 'U', 'V', 'W', 'X', 'Y', '1', '8']
c = ['E', 'J', 'S', 'Z']
d = ['3', 'L', '2', '5']
a = input()
cnt = 3
for i in range (len(a)):
    if a[i] != a[-i - 1]:
        if cnt == 3:
            cnt = 1
        if cnt == 2:
            cnt = 0
        if a[i] not in c:
            if a[i] not in d:
                if cnt == 1:
                    cnt = 0
            else:
                if (d.find(a[i]) != c.find(a[-1 - i])):
                    if cnt == 1:
                        cnt = 0
        else:
            if (c.find(a[i]) != d.find(a[-1 - i])):
                if cnt == 1:
                    cnt = 0
    else:
        if (a[i] not in b):
            if cnt == 3:
                cnt = 2
print (cnt)
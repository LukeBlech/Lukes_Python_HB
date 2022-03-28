a = 7
b = 10
c = []
for i in range(a,b+1):
    if not i in c:
        c.append(i)
print(c)
#return list(range(a,b+1))
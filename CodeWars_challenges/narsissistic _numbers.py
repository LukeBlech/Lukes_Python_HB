n = 153
q = list(map(int, str(n)))
c = []
for i in q:
    i = i ** len(q)
    c.append(i)
if n == sum(c):
    print(True)
else:
    print(False)
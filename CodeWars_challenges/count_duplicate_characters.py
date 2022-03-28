string = "RroOom"
string = string.lower()
c = []
u = 0
for i in string:
    if (string.count(i)) >= 2:
        if i not in c:
            c.append(i)
for i in c:
    u = u + 1
print(u)

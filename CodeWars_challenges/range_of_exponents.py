n = 4
c = [2]
q = []
for i in c:
    if n != -1:
        q.append(2**n)
        c.append(2 ** n)
        n = n-1
q.reverse()
print(q)

#def powers_of_two(n):
    #return [2**x for x in range(n+1)]
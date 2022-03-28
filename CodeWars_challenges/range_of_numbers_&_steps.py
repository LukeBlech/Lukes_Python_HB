generate_range = (-10, 10, 1)
c = []
for i in range(generate_range[0], generate_range[1]):
    if not i in c:
        c.append(i)
print(c[::generate_range[2]])

#def generate_range(x,y,z):
    #return [ i for i in range(x,y,z)]
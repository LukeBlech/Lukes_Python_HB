geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
birds = ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
c = []
for x in birds:
    if x not in geese:
        c.append(x)
return(c)
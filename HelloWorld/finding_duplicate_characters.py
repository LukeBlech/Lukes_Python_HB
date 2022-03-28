string = "Rom"
string = string.lower()
c = True
for i in string:
    if (string.count(i)) >= 2:
        c = False
print(c)

#def is_isogram(string):
    #return len(string) == len(set(string.lower()))
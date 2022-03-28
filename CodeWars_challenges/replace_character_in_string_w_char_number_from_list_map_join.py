string = "The sunset sets at twelve o' clock."
string = string.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
c = []
for i in list(string):
    if i in list(alphabet):
        c.append(alphabet.find(i) + 1)
c = map(str, c)
c = " ".join(c)
print(str(c))
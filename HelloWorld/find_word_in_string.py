sentence = "EnGlish"
sentence = sentence.lower()
sentence = sentence + "random"
c = False
x = sentence.find("english")
if x != -1:
    c = True
print(c)
print(x)

#short
#return'english' in sentence.lower()
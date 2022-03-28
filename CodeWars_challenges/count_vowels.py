input_str = "luxurious banana"
vowels = "a", "e", "i", "o", "u"
c = 0
input_str.lower()
for i in input_str:
    if i in vowels:
        c = c + 1
print(c)

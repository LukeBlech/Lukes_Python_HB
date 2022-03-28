seq = ["anyone", "want", "to", 8, "hire", "me?"]
elem = 8
torf = False
for ele in seq:
    if elem in seq:
        torf = True
print(torf)
#return elem in seq
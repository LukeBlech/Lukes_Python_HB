x = ['Petes kata', 'kata', 'Petes kata', 'life', 'kata', 'Petes kata', 'eating', 'eating', 'Petes kata', 'kata', 'life', 'life', 'life', 'life', 'life', 'Petes kata', 'Petes kata', 'Petes kata', 'Petes kata', 'Petes kata', 'Petes kata', 'eating', 'eating', 'kata', 'eating', 'kata']
kata = 0
petes_kata = 0
life = 0
eating = 0
for i in x:
    if "kata" in x:
        kata = + (x.count('kata')) * 5
    if 'Petes kata' in x:
        petes_kata = + (x.count('Petes kata')) * 10
    if 'eating' in x:
        eating = + (x.count('eating')) * 1
    if 'life' in x:
        life = + (x.count('life')) * 0
c = kata + petes_kata + life + eating
if c < 40:
    print('Super happy!')
if c > 40:
    if c < 70:
        print('Happy!')
if c > 70:
    if c < 100:
        print('Sad!')
if c > 100:
    print('Miserable!')
print(c)

#def paul(x):
    #the *5 + x.count("Petes kata")*10 + x.count("eating")
    #return  'Super happy!' if val<40 else 'Happy!' if 40<=val<70 else  'Sad!' if 70<=val<100 else  'Miserable!'
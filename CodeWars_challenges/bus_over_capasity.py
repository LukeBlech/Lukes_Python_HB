cap = 100
on = 50
wait = 6
if on + wait <= cap:
    print(0)
if on + wait > cap:
    print((cap - on - wait) * -1)

    #def enough(cap, on, wait):
    #return max(0, wait - (cap - on))
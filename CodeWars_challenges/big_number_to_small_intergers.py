def digitize(n):
    if n == 0:
        return[0]
    else:
        digits = []
        while n > 0:
            digits.append(n % 10)
            n = (n - n % 10) // 10
        return(digits[::-1])

#def digitize(n):
    #return list(map(int, str(n)))cc
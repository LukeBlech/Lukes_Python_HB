#kpl = float(input())
def converter(mpg):
    km = 1.609344
    kpl = mpg * km * 0.2199691573325614
    return(kpl.__round__(2))
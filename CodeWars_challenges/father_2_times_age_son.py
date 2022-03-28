def twice_as_old(dad_years_old, son_years_old):
    diff = dad_years_old - son_years_old
    birth = 0
    while diff != birth * 2:
        birth = birth + 1
        diff = diff + 1
    result = dad_years_old - diff
    if result < 0:
        result = result * -1
    return(result)

#def twice_as_old(dad_years_old, son_years_old):
    #return abs(dad_years_old - 2*son_years_old)

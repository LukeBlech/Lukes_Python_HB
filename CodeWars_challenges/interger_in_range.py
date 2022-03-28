#age = 14
#drink = 0
#if age < 14:
    #drink = 'drink toddy'
#if age >= 14:
    #if age < 18:
        #drink = 'drink coke'
#if age >= 18:
    #if age < 21:
        #drink = 'drink beer'
#if age >= 21:
    #drink = 'drink whisky'
#print(drink)

def people_with_age_drink(age):
    if age > 20: return 'drink whisky'
    if age > 17: return 'drink beer'
    if age > 13: return 'drink coke'
    return 'drink toddy'

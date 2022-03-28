temp = input("What is the temperature? " )
unit = input("fahrenheit (f) or celsius (c)? ")
if unit.upper() == 'F':
    convert = (float(temp) - 32) * .555
    print("The temperature in celsius is: " + str(convert))
else:
    convert = (float(temp) * 1.8) + 32
    print("The temperature in fahrenheit is: " + str(convert))

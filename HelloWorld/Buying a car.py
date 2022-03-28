startPriceOld = 2000
startPriceNew = 8000
savingperMonth = 1000
percentLossByMonth = 1.5
savings = startPriceOld
c = 0
months = 0
while savings < startPriceNew:
    if savings <= startPriceNew:
        savings = savings + savingperMonth
        startPriceOld = startPriceOld - (startPriceOld * (percentLossByMonth/100))
        startPriceNew = startPriceNew - (startPriceNew * (percentLossByMonth/100))
        c = c + 0.25
        months = months + 1
        if c == 0.5:
            percentLossByMonth = percentLossByMonth + c
            c = 0
print((savings - startPriceNew), months)

#not quite finished

human_years = 10
catYears_1st_year = 15
catYears_2nd_year = 9
catYears_older = 4
dogYears_1st_year = 15
dogYears_2st_year = 9
dogYears_older = 5
if human_years == 1:
    print(human_years, catYears_1st_year, dogYears_1st_year)
if human_years == 2:
    print(human_years, catYears_1st_year + catYears_2nd_year, dogYears_1st_year + dogYears_2st_year)
if human_years > 2:
    print(human_years, catYears_1st_year + catYears_2nd_year + (catYears_older * (human_years - 2)), dogYears_1st_year + dogYears_2st_year + (dogYears_older * (human_years - 2)))
#def human_years_cat_years_dog_years(x):
    #return [x, 24+(x-2)*4 if (x != 1) else 15, 24+(x-2)*5 if (x != 1) else 15]
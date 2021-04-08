def feb(year):
    if year % 4 == 0 and not year % 100 == 0:
        FebDays = 29
    elif year % 400 == 0:
        FebDays = 29
    else:
        FebDays = 28
    return FebDays

def CountingSundays(startday,startyear,endyear):
    months = {'jan':31, 'feb':'oopsies', 'mar':31, 'apr':30, 'may':31, 'jun':30, 'jul':31, 'aug':31, 'sep':30, 'oct':31, 'nov':30, 'dec':31,}
    Sundays = 0
    year = startyear
    day = startday
    while year <= endyear:
        if day == 1:
            Sundays += 1
        for LastMonth in months.keys():
            if LastMonth == 'feb':
                MonthDays = feb(year)
            else:
                MonthDays = months.get(LastMonth)
            modulus = MonthDays % 7
            if day + modulus > 7:
                day = day + modulus - 7
            else:
                day += modulus 

            if day == 1 and not LastMonth == 'dec':
                Sundays += 1
            if LastMonth == 'dec':
                year += 1
    return Sundays

day = 2
modulus = 365 % 7
if day + modulus > 7:
    day = day + modulus - 7
else:
    day += modulus

print(CountingSundays(day,1901,2000))
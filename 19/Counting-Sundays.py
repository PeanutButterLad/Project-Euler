# An important note to understand this code is that I arbitrarily assigned the days Sunday-Saturday the numbers 1-7. This keeps things simpler.
# The overall idea is to brute force an answer by adding the total days of each month to the start date then checking if the first of the next month is a sunday. 
# Except it's way more optimized than that.

# A funcion to figure out how many days February has in a given year.
def feb(year):
    if year % 4 == 0 and not year % 100 == 0:
        FebDays = 29
    elif year % 400 == 0:
        FebDays = 29
    else:
        FebDays = 28
    return FebDays

# The main funcion
def CountingSundays(startday,startyear,endyear):
    # There is definetly a more optimized way to organize the months other than a dictionary, but it is probably only marginally better.
    months = {'jan':31, 'feb':'oopsies', 'mar':31, 'apr':30, 'may':31, 'jun':30, 'jul':31, 'aug':31, 'sep':30, 'oct':31, 'nov':30, 'dec':31,}
    Sundays = 0
    year = startyear
    day = startday
    while year <= endyear:
        # Starting with this because the date we start with is Jan 1, so each month we iterate through is actually the last month. 
        # This is important once we hit December.
        if day == 1:
            Sundays += 1
        # Loop through the months
        for LastMonth in months.keys():
            if LastMonth == 'feb':
                MonthDays = feb(year)
            else:
                MonthDays = months.get(LastMonth)
            # Divide the days of the month by 7. 
            # The remainder is how many days difference there is between whatever weekday it started on and the first day of the next month
            modulus = MonthDays % 7
            # If the current day plus the remainder from last month is greater than 7 then we subtract 7 from the total.
            if day + modulus > 7:
                day = day + modulus - 7
            else:
                day += modulus 
            # If last month was December then the current month is january of the next year. 
            # So we don't want to count this day if it is a Sunday until next 'year' or next iteration of the while loop.
            # (In a very rare case you might add a sunday that falls on Jan 1 of the year after your endyear, this is to avoid that)
            if day == 1 and not LastMonth == 'dec':
                Sundays += 1
            if LastMonth == 'dec':
                year += 1
    return Sundays

# This is just to get the first day of 1901 from the first day of 1900
day = 2
modulus = 365 % 7
if day + modulus > 7:
    day = day + modulus - 7
else:
    day += modulus

# Print our called function
print(CountingSundays(day,1901,2000))

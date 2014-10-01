def is_leap_year(year):
    result = False

    if year % 100 == 0 and year % 400 == 0:
        result = True
    elif year % 4 == 0:
        result = True

    return result

def get_next_day(current_day):
    if current_day == 7:
        return 1

    return current_day + 1

today = 2
first_of_month_sunday = 0

for year in xrange(1901, 2000 + 1):
    for month in xrange(1, 12 + 1):
        february_days = 29 if is_leap_year(year) else 28
        days = {
                1: 31,
                2: february_days,
                3: 31,
                4: 30,
                5: 31,
                6: 30,
                7: 31,
                8: 31,
                9: 30,
                10: 31,
                11: 30,
                12: 31,
            }

        for day in xrange(1, days[month] + 1):
            if day == 1 and today == 7:
                first_of_month_sunday += 1

            today = get_next_day(today)

print first_of_month_sunday

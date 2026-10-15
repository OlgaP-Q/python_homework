def is_year_leap(year):
    return year % 4 == 0


year = 2025
is_leap = is_year_leap(year)
print(f'Год {year}: {is_leap}')

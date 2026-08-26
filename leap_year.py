def leap_year(year):
    if year < 0:
        return "Invalid year"
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return "Leap year"
    else:
        return "Not a leap year"

year = int(input("Enter a year: "))
result = leap_year(year)
print("The year is:", result)
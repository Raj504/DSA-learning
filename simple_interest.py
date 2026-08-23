def simple_interest(principle, rate, time):
    if principle < 0 or rate < 0 or time < 0:
        return "Principle, rate, and time cannot be negative"
    interest = (principle * rate * time)/100
    return round(interest, 2)

principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
interest = simple_interest(principle, rate, time)
total = principle + interest
print("The simple interest is:", interest)
print("The total amount is:", total)
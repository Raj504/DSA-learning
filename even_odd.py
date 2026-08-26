def even_odd(num):
    if num < 0:
        return "Negative"
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(float(input("enter a number: ")))
result = even_odd(number)
print("The number is:", result)
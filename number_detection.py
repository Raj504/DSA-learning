def number_detection(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    else:
        return "Zero"


number = float(input("Enter a number: "))
result = number_detection(number)
print("Number is:", result)
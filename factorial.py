def factorial(n):
    if n < 0:
        return "Please enter a non-negative integer."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result


number = int(float(input("Enter a number: ")))
result = factorial(number)
print("The factorial of", number, "is:", result)
def add_two_number(a, b):
    add = a + b
    return add

def subtract_two_number(a, b):
    subtract = a - b
    return subtract

def multiply_two_numbers(a,b):
    multiply = a * b
    return multiply

def divide_two_numbers(a, b):
    divide = a / b
    return divide

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
result1 = add_two_number(number1, number2)
result2 = subtract_two_number(number1, number2)
result3 = multiply_two_numbers(number1, number2)
result4 = divide_two_numbers(number1, number2)
print("The sum is:", result1)
print("The difference is:", result2)
print("The product is:", result3)
print("The quotient is:", result4)
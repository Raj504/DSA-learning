def print_numbers(n):
    if n < 1:
        print("Please enter a positive integer.")
        return
    for i in range(1, n + 1):
        print(i)

number = int(float(input("Enter a number: ")))
print_numbers(number)
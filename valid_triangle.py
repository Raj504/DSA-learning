def valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid triangle"
    if (a + b > c) and (a + c > b) and (b + c > a):
        return "Valid triangle"
    else:
        return "Invalid triangle"

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

result = valid_triangle(side1, side2, side3)
print("The triangle is:", result)
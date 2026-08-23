import math

def circle_radius(radius):
    if radius < 0:
        return "Radius cannot be negative"
    area = math.pi * radius * radius
    return round(area, 2)

radius = float(input("Enter the radius of the circle: "))
area = circle_radius(radius)
print("the area of the circle is:", area)
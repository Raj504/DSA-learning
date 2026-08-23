def celius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return "Temperature below -273.15 is not possible"
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = celius_to_fahrenheit(celsius)
print("Temperature in fahrenheit:", fahrenheit)
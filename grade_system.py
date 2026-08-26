def grade_system(score):
    if score < 0 or score > 100:
        return "Invalid marks"
    if score < 60:
        return "F"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    else:
        return "A"

score = float(input("Enter your score: "))
result = grade_system(score)
print("Your grade is:", result)
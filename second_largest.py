def second_largest(s):
    digits = []
    for char in s:
        if char.isdigit():
            digits.append(int(char))

    digits = list(set(digits))  
    if len(digits) <2:
        return -1
    # Assume first two as largest and second largest
    if digits[0] > digits[1]:
        first = digits[0]
        second = digits[1]
    else:
        first = digits[1]
        second = digits[0]

    for i in range(2, len(digits)):
        if digits[i] > first:
            second = first
            first = digits[i]
        elif digits[i] > second:
            second = digits[i]
    return second

s = "dfa123738821afd"
print(second_largest(s))  

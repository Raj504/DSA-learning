def palindrome(x):
    if x<0:
        return False
    
    x_copy = x
    rev = 0

    while x_copy>0:
        rem = x_copy % 10
        rev = rev * 10 + rem
        x_copy = x_copy // 10
    return rev == x

print(palindrome(121))
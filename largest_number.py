def largest_number(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num
    return largest

numbers = [3, 5, 2, 8, 1]
print("The largest number is:", largest_number(numbers))
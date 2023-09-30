"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        length = len(numbers)
        if len(numbers)%2 == 1:
            print(f'The median is: {numbers[length//2]}') 
        else:
            num1 = numbers[(length//2) - 1]
            num2 = numbers[(length//2)]        
            temp = (num2 - num1) / 2
            median = num1 + temp
            print(f'The median is: {median}')


    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

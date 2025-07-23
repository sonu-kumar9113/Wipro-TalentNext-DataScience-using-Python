# Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
# lastDigit(7, 17) → true
# lastDigit(6, 17) → false
# lastDigit(3, 113) → true

a = int(input())
b = int(input())
if a % 10 == b % 10:
    print("true")
else:
    print("false")

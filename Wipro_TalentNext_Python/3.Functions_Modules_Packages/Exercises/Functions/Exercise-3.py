# Write a function to calculate and return the factorial of a number (a non-negative integer).

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))

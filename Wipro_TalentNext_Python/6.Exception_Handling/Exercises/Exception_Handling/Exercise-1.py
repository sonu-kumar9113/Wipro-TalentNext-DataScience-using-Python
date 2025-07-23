# Write a program to accept two numbers from the user and perform division. 
# If any exception occurs, print an error message or else print the result.

try:
    a = int(input())
    b = int(input())
    result = a / b
    print(result)
except Exception as e:
    print("Error:", e)

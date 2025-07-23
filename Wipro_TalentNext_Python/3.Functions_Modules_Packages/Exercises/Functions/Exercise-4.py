# Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.

def count_case(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("Upper case letters:", upper)
    print("Lower case letters:", lower)

count_case("Hello World!")

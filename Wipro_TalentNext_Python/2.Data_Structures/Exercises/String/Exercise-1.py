# Write a program to count the number of upper and lower case letters in a String.

s = "Hello World"
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")

# Write a program to print the sum of all the digits of a given number.

# Example:
# I/P:1234
# O/P:10

n = int(input())
s = 0
while n > 0:
    s += n % 10
    n //= 10
print(s)

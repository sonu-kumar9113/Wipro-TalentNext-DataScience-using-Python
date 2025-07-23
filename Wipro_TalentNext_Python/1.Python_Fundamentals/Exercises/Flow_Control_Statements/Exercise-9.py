# Write a program to reverse a given number and print.

# Example:1
# I/P: 1234
# O/P:4321

# Example:2
# I/P:1004
# O/P:4001

n = int(input())
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)

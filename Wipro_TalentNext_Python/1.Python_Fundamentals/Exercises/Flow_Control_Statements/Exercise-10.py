# Write a program to find if the given number is palindrome or not.

# Example:1
# I/P:110011
# O/P: 110011 is a palindrome.

# Example:2
# I/P:1234
# O/P: 1234 is not a palindrome.

n = int(input())
temp = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
if temp == rev:
    print(f"{temp} is a palindrome.")
else:
    print(f"{temp} is not a palindrome.")

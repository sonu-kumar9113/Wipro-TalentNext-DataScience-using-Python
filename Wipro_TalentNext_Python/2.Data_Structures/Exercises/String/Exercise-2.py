# Write a program that will check whether a given String is Palindrome or not.

s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

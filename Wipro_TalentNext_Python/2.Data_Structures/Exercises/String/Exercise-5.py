# Given a string and an integer n, return a string made of n repetitions of the last n 
# characters of the string.

s = "Wipro"
n = 3
result = s[-n:] * n
print(result)

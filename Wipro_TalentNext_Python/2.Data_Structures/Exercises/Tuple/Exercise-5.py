# Write a program to replace last value of tuples in a list to 100.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
result = [(x[0], x[1], 100) for x in lst]
print(result)

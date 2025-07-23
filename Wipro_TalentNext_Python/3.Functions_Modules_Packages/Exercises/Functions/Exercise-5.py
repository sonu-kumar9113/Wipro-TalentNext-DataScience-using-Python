# Write a function to print the even numbers from a given list. List is passed to the function as an argument.

# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result: [2, 4, 6, 8]

def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

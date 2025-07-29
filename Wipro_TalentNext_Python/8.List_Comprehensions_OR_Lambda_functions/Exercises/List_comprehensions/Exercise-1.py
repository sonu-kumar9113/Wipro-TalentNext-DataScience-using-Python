# Write a LC program to create an output dictionary which contains only the odd numbers 
# that are present in the input list = [1,2,3,4,5,6,7] as keys and their cubes as values

input_list = [1,2,3,4,5,6,7]
output = {x: x**3 for x in input_list if x % 2 == 1}
print(output)

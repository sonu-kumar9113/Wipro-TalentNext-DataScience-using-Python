# Write a program to iterate over a dictionary using for loop and print the keys alone, 
# values alone and both keys and values.

d = {1: 10, 2: 20, 3: 30}
for k in d:
    print(k)
for v in d.values():
    print(v)
for k, v in d.items():
    print(k, v)

# Write a program to accept the file name to be opened from the user, if file exist print the 
# contents of the file in title case or else handle the exception and print an error message.

try:
    filename = input()
    with open(filename, 'r') as f:
        data = f.read()
        print(data.title())
except:
    print("Error: File not found")

# Write a program to read the entire content from a .txt file and display it to the user.

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

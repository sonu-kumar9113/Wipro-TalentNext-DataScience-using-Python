# Write a program to accept input from user and append it to a .txt file.

text = input()
with open("sample.txt", "a") as file:
    file.write(text + "\n")

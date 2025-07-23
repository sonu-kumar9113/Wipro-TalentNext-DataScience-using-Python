# Write a program to read contents from a .txt file line by line and store each line into a list.

with open("sample.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    print(lines)

# Write a program to read first n lines from a .txt file. Get n as user input.

n = int(input())
with open("sample.txt", "r") as file:
    for i in range(n):
        line = file.readline()
        print(line.strip())

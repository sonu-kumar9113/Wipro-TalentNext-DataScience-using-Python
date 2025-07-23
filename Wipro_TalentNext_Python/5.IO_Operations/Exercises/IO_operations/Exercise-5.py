# Write a program to find the longest word from the .txt file contents, assuming that the file will have only one longest word in it.

with open("sample.txt", "r") as file:
    words = file.read().split()
    longest = max(words, key=len)
    print(longest)

# Write a program to count the frequency of a user entered word in a .txt file.

word = input()
with open("sample.txt", "r") as file:
    content = file.read().split()
    count = content.count(word)
    print(count)

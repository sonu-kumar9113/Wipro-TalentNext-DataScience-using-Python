# Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. 
# If any invalid index is entered, handle the exception and print an error message.

numbers = [10, -3, 7, -8, 5, -1, 6, -9, 2, 4]
try:
    index = int(input())
    value = numbers[index]
    if value >= 0:
        print("Positive")
    else:
        print("Negative")
except:
    print("Error: Invalid index")

# Write a program to accept a number from the user and check whether it’s prime or not. 
# If user enters anything other than number, handle the exception and print an error message.

try:
    num = int(input())
    if num < 2:
        print("Not Prime")
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
except:
    print("Error: Invalid input")

# Write a program to check if a given number is prime or not.

n = int(input())
if n < 2:
    print("Not Prime")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

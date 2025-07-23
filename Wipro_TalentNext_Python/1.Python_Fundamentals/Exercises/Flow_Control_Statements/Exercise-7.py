# Write a program to print prime numbers between 10 and 99.

for num in range(10, 100):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

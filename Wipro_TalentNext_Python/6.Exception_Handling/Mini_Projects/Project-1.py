# You had saved the items and their price details in a text file, 
# which you purchased yesterday from a nearby super market.

# You need to know:
# How many items did you purchase?
# How many items are free?
# What is the total amount you had to pay?
# What is the discount amount?
# What is the final amount did you pay after the discount?

# Note:
# Data is stored in a text file Purchase-1.txt.
# Each line contains one item’s details.
# Item name and price is separated by a space.
# You have to enter the file name during run time.

try:
    filename = input("Enter the file name: ")
    with open(filename + ".txt", 'r') as f:
        lines = f.readlines()

    items_purchased = 0
    free_items = 0
    total_amount = 0
    discount = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) == 2:
            name, price = parts[0], parts[1]
            if price.lower() == 'free':
                free_items += 1
            elif name.lower() == 'discount':
                discount = int(price)
            else:
                items_purchased += 1
                total_amount += int(price)

    final_amount = total_amount - discount

    print("No of items purchased:", items_purchased)
    print("No of free items:", free_items)
    print("Amount to pay:", total_amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("Error: File not found")
except ValueError:
    print("Error: Invalid data in file")
except Exception as e:
    print("Error:", e)


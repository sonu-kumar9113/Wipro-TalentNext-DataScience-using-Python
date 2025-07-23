# Let's assume you are planning to use your Python skills to build a PBLApp for Mobile.
# You decide to host your application on servers running in the cloud. 
# You pick a hosting provider that charges $0.51 per hour. 
# You will launch your service using one server and want to know how much it will cost to operate per day, per week, per month.

# Write a Python program that displays the answers to the following questions:

# How much does it cost to operate one server per day?
# How much does it cost to operate one server per week?
# How much does it cost to operate one server per month?
# How many days can I operate one server with $918?

cost_per_hour = 0.51
cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30
budget = 918
days_possible = budget / cost_per_day
print("Cost per day:", cost_per_day)
print("Cost per week:", cost_per_week)
print("Cost per month:", cost_per_month)
print("Days with $918:", int(days_possible))

# Given a string of n words, help Alex to find out how many times his name appears in the string.

# Constraint: 1 <= n <= 200

# Sample input: Hi Alex WelcomeAlex Bye Alex.
# Sample output: 3

# Explanation:
# Alex name appears 3 times in the string. Hi Alex WelcomeAlex Bye Alex.


text = "Hi Alex WelcomeAlex Bye Alex"
count = text.count("Alex")
print(count)

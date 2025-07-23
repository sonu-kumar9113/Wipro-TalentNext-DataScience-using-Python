import mymodule

name1 = "bob"
if mymodule.ispalindrome(name1):
    print("Yes it is a palindrome.")
else:
    print("No it is not a palindrome.")
print("No of vowels:", mymodule.count_the_vowels(name1))
freq1 = mymodule.frequency_of_letters(name1)
print("Frequency of letters:", ', '.join(f"{k}-{v}" for k, v in freq1.items()))

print()

name2 = "marcel bentok tanaka"
if mymodule.ispalindrome(name2):
    print("Yes it is a palindrome.")
else:
    print("No it is not a palindrome.")
print("No of vowels:", mymodule.count_the_vowels(name2))
freq2 = mymodule.frequency_of_letters(name2)
print("Frequency of letters:", ', '.join(f"{k}-{v}" for k, v in freq2.items()))

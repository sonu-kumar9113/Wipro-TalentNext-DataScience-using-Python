def ispalindrome(name):
    name = name.replace(" ", "")
    return name == name[::-1]

def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in name if char in vowels)

def frequency_of_letters(name):
    freq = {}
    for char in name.replace(" ", ""):
        freq[char] = freq.get(char, 0) + 1
    return freq

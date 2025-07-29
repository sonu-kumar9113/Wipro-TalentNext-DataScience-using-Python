# Split the following irregular sentence into proper words
# sentence = """A, very    very; irregular_sentence"""  
## expected outout : A very very irregular sentence


import re
sentence = """A, very    very; irregular_sentence"""
print(" ".join(re.findall(r'\w+', sentence)))

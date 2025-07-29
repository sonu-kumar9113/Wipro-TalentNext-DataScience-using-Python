# Given below list of words, identify the words that begin and end with the same character.
# civic  
# trust  
# widow  
# maximum
# museums
# aa 
# as


import re
words = ['civic', 'trust', 'widow', 'maximum', 'museums', 'aa', 'as']
print([w for w in words if re.fullmatch(r'(.).*\1', w)])

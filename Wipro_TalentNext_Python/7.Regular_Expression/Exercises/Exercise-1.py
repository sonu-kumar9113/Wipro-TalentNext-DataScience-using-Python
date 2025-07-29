# Write a program to find check if a string has only octal digits. 
# Given string ['789','123','004']

import re
lst = ['789', '123', '004']
res = [s for s in lst if re.fullmatch(r'[0-7]+', s)]
print(res)
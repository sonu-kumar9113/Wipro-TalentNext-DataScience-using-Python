# Given a string, if the first or last character is 'x', return the string without those 'x' 
# character, else return the string unchanged.

s = "xHix"
if s.startswith('x'):
    s = s[1:]
if s.endswith('x'):
    s = s[:-1]
print(s)

# Make a dictionary of the 26 English alphabets mapping each with the corresponding integer

output = {chr(i+97): i+1 for i in range(26)}
print(output)

# Extract the user id, domain name and suffix from the following email addresses.
# emails = """zuck@facebook.com  
# sunder33@google.com  
# jeff42@amazon.com"""


import re
emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""
print(re.findall(r'([\w\d]+)@([\w\d]+)\.(\w+)', emails))

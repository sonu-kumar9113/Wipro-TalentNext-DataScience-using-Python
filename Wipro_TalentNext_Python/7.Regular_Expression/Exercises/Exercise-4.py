# Clean up the following tweet so that it contains only the user’s message. 
# That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.

# #tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today  
# http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''  

##desired_output = 'Good advice What I would do differently if I was learning to code today'

import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
tweet = re.sub(r'http\S+|@\w+|#\w+|RT|cc|[:!]', '', tweet)
print(tweet.strip())


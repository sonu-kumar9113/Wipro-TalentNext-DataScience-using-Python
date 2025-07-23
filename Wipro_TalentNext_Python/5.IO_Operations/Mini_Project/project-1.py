# Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.
# He challenges you to find it out without seeing the content of the file. He has given hints to find it. Let’s surprise him by breaking the challenge with our python code.

# Hints to find the secret message:
# The number of lines in the file tells you the meeting time.
# Note: 1 <= number of lines <= 24

# If the number of lines is exceeding 12, you need to convert it to 12 hour format. 
#For example,
# If the number of lines is 15, then the meeting time is 3 PM.
# If the number of lines is 10, then the meeting time is 10 AM.

# The word appearing for the maximum number of times tells you the meeting place.
# Note: Meeting place will be a street name.
# For example,
# If the word Oxford appears for the maximum number of times, then meeting place is Oxford Street.
# If the word Park appears for the maximum number of times, then meeting place is Park Street.

from collections import Counter

with open("sample.txt", "r") as file:
    lines = file.readlines()

line_count = len(lines)
meeting_hour = line_count % 12
if meeting_hour == 0:
    meeting_hour = 12
meeting_time = f"{meeting_hour} {'PM' if line_count > 12 else 'AM'}"

text = ' '.join(lines)
words = text.split()
word_counts = Counter(words)
most_common_word = word_counts.most_common(1)[0][0]

print(f"Meeting time: {meeting_time}")
print(f"Meeting place: {most_common_word} Street")


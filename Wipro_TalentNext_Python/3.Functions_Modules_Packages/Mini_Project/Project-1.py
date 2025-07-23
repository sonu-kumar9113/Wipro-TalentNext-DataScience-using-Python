# Write a Python function that accepts a hyphen-separated sequence of colors as input and returns
# the colors in a hyphen-separated sequence after sorting them alphabetically.

# Constraint: All the colors will be completely in either lower case or upper case.

# Sample input 1:
# green-red-yellow-black-white
# Sample output 1:
# black-green-red-white-yellow

# Sample input 2:
# PINK-BLUE-TAN-PURPLE
# Sample output 2:
# BLUE-PINK-PURPLE-TAN


def sort_colors(color_sequence):
    colors = color_sequence.split('-')
    colors.sort()
    return '-'.join(colors)

# Example usage
print(sort_colors("green-red-yellow-black-white"))
print(sort_colors("PINK-BLUE-TAN-PURPLE"))

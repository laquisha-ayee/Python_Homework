# It's time to explore the *list* object and how to use it Follow the
# instructions in the code comments. Be sure to test your work by running your
# code!

# DO NOT EDIT - Starting with a simple lists of colors and numbers
colors = ["blue", "Green", "PURPLE", "blue-green", "sky blue"]
numbers = [2, 34, 8.5, -22.0, 33//4, 2**5]
print ('COLORS', colors)
print ('NUMBERS', numbers)

# 1. Print the total number of colors (length of the list)
print('total number of colors:', len(colors))

# 2. Print the first color
print('first color:', colors[0])

# 3. Print the second and third colors
print('second and third colors:', colors[1:3])

# 4. Print the last two colors
print('last two colors:', colors[-2:])

# 5. Print the smallest number in the numbers list
print('smallest number:', min(numbers))

# 6. Print the largest number in the numbers list
print('largest number:', max(numbers))

# 7. Sort the numbers list
numbers.sort()
print ('SORTED NUMBERS', numbers)

# 8. Sort the colors alphabetically ignoring case
colors.sort(key=str.lower)
print ('SORTED COLORS', colors)

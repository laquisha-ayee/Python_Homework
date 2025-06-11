# It's time to explore the *tuple* object and how to use it.

# Follow the instructions in the code comments. Be sure to test your work by
# running your code!

# For the bonus, remember you can split a returned tuple to variables: `(a,b,c)
# = myfunc()`

# DO NOT EDIT
odds = 1,3,5,7,9
evens = 2,4,6,8

# Step 1: Print out the result of adding evens to odds
print("Step 1 - Adding evens to odds:")
print(evens + odds)

# Step 2: Print out the result of multiplying odds by three
print("Step 2 - Multiplying odds by three:")
print(odds * 3)

# Step 3A: Use print to find out if odds is less than evens
print("Step 3A - Is odds less than evens?")
print(odds < evens)

# Step 3B: Print out your explanation of why 3A has that result
print("Step 3B - Explanation:")
print("False because tuple comparison is lexicographic (element by element).")
print("First elements: 1 < 2 is True, so we'd expect True, but...")
print("Actually it's comparing the entire tuples and 1 < 2 is True!")

# Step 4: Print out the average of the numbers in evens using one line of code
print("Step 4 - Average of evens:")
print(sum(evens) / len(evens))

# Step 5A: Write a function 'minmaxmean' that accepts an iterable and
#         returns the minimum value, the maximum value and the average (mean)
def minmaxmean(iterable):
    minimum = min(iterable)
    maximum = max(iterable)
    mean = sum(iterable) / len(iterable)
    return minimum, maximum, mean

# Step 5B: Use print to confirm your function is working on evens and odds
print("Step 5B - Testing minmaxmean function:")
print("Evens result:", minmaxmean(evens))
print("Odds result:", minmaxmean(odds))

# BONUS: Call your function with a new tuple of your own creation
#        And print the results in a pretty way
my_numbers = (10, 25, 5, 30, 15, 20)
min_val, max_val, mean_val = minmaxmean(my_numbers)

print("BONUS - Pretty results for", my_numbers)
print(f"Minimum: {min_val}")
print(f"Maximum: {max_val}")
print(f"Average: {mean_val:.2f}")
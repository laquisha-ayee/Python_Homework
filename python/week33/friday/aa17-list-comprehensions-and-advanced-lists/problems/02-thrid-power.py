# Create a function that takes in a  list, `lst` and returns the values
# multiplied to the third power. Hint: This should be a single line of code by
# using list comprehensions.

# Write your function here.
def third(lst):
    result = []
    for i in range(len(lst)):
        cubed_value = lst[i] ** 3
        result.append(cubed_value)
    return result

print(third([2, 4, 8])) #> [8, 64, 512]
print(third([3, 5, 6])) #> [27, 125, 216]
print(third([1, 3, 7])) #> [1, 27, 343]
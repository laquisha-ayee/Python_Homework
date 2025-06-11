# Create a function that returns True if the first list can be nested inside the
# second. 

# list1 can be nested inside list2 if: 
# - list1's min is greater than list2's min
# - list1's max is less than list2's max 

# You may want to consider writing a couple of functions to organize your thoughts better.

# Write your code here.
def get_min_max(lst):
    return min(lst), max(lst)

def can_nest(list1, list2):
    min1, max1 = get_min_max(list1)
    min2, max2 = get_min_max(list2)
    return min1 > min2 and max1 < max2


print(can_nest([1, 2, 3, 4], [0, 6]))  #> True
print(can_nest([3, 1], [4, 0]))        #> True
print(can_nest([9, 9, 8], [8, 9]))     #> False
print(can_nest([1, 2, 3, 4], [2, 3]))  #> False
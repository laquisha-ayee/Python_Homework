# Create a function that takes in a `tuple` of tuples with varying lengths, a
# given `value`, and a given `length`. The function should return a copy of
# tuple where each nested tuple has the specified `length`. To increase a
# tuple's length, the function should append the value the necessary number of
# times. (You may assume that all tuples originally in the tuple have a length
# <= `length`.)

# Write your function here.
def fill_tuple(tuple_of_tuples, value, length):
    result = []
    for nested_tuple in tuple_of_tuples:
        current_length = len(nested_tuple)
        if current_length < length:
            elements_to_add = length - current_length
            new_tuple = nested_tuple + (value,) * elements_to_add
        else:
            new_tuple = nested_tuple
        result.append(new_tuple)
    return tuple(result)




print(fill_tuple(((58, 1, 5), (0, 3), (45, ), (24, 23)), 2, 3))    #> ((58, 1, 5), (0, 3, 2), (45, 2, 2), (24, 23, 2))
print(fill_tuple(((1, ), (5, 7), (55, 22), (80, 52, 20)), 5, 4))   #> ((1, 5, 5, 5), (5, 7, 5, 5), (55, 22, 5, 5), (80, 52, 20, 5))
print(fill_tuple(((), (0, 14), (5, 2, 8), (2, 4, 2, 3)), 0, 5))    #> ((0, 0, 0, 0, 0), (0, 14, 0, 0, 0), (5, 2, 8, 0, 0), (2, 4, 2, 3, 0))
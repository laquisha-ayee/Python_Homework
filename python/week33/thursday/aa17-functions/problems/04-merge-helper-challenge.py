# Recall the merge sort algorithm:
    
# 1. Find midpoint to divide list in half
# 2. Call `merge_sort` recursively on the first half
# 3. Call `merge_sort` recursively on the second half
# 4. Merge the two sorted halves with `merge`

# Implement the `merge_sort` function with the `merge` helper function.

# Write your code here.
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2

    first_half = merge_sort(lst[:mid])
    second_half = merge_sort(lst[mid:])

    return merge(first_half, second_half)

def merge(first_half, second_half):
    result = []
    i = j = 0

    while i < len(first_half) and j < len(second_half):
        if first_half[i] <= second_half[j]:
            result.append(first_half[i])
            i += 1
        else:
            result.append(second_half[j])
            j += 1


    while i < len(first_half):
        result.append(first_half[i])
        i += 1

    while j < len(second_half):
        result.append(second_half[j])
        j += 1

    
    return result





lst = [5, 2, 38, 91, 16, 427]

sorted_lst = merge_sort(lst)        # Out of place solution
print(sorted_lst)                  


lst[:] = merge_sort(lst)            # In place solution
print(lst)                       
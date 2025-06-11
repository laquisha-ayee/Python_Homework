# Create a function that uses the insertion sort algorithm to sort the list.

# Write your function here.
def insertion_sort(lst):
    arr = lst.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1     

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    
    return arr




print(insertion_sort([55, 21, 5, 3, 6, 95])) #> [3, 5, 6, 21, 55, 95]
print(insertion_sort([4, 1, 0, 3, 8, 9])) #> [0, 1, 3, 4, 8, 9]
print(insertion_sort([1, 4, 3, 0, 3, 0, 2, 8])) #> [0, 0, 1, 2, 3, 3, 4, 8]
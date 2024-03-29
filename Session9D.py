# SORTING ALGORITHMS
# SELECTION SORT
# Repeatedly finding the minimum element and putting it in beginning
# Selection
# Swapping
# Counter Shift

arr = [64, 25, 12, 22, 11]
# Traverse through all array elements
for i in range(len(arr)):
    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    # Swap the found minimum element with the first element
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # Driver code to test above
print("Sorted array")
for i in range(len(arr)):
    print("%d" % arr[i])
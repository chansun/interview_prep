def partition(arr, start, end):
    pivot = arr[end] # choose a pivot
    left = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[left] = arr[left], arr[i] # swap
            left += 1 # update left index
    arr[end], arr[left] = arr[left], arr[end] # swap
    return left # pivot index

def quickSort(arr, start, end):
    if start < end:
        mid = partition(arr, start, end)
        quickSort(arr, start, mid-1) # sort left sub-array
        quickSort(arr, mid+1, end) # sort right sub-array

arr = [9,8,7,6,5,4,300, 1]
quickSort(arr, 0, len(arr)-1)
print(arr)

# Performance
    # Time complexity
        # Avg. case
            # O(N log N)
        # Worst case (if chose the worst pivot)
            # O(N^2)
    # Space complextiy
        # Avg. case
            # O(log N) if the depth of the recursion is log N.
        # Worst case (if chose the worst pivot)
            # O(N) if depth of the recursion is N.

        
        
        
        
arr = [1, 7, 8, 9, 13, 15, 24] # Caution: arr should be sorted in ascending order to use binary search!

def binary_search(arr, target, start, end):
    if start > end:
        return "None"
    else:
        mid = int((start + end)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target: # move to the left
            return binary_search(arr, target, start, mid-1)
        elif arr[mid] < target: # move to the right
            return binary_search(arr, target, mid+1, end)
        

print(binary_search(arr, 13, 0, len(arr)-1))
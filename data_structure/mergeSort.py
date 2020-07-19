def mergeSort(arr):
    if len(arr) > 1:
        mid = int(len(arr)/2)
        left = arr[:mid]
        right = arr[mid:]
        
        # dividing phase
        mergeSort(left)
        mergeSort(right)
        
        # combining phase
        l = r = k = 0
        
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                arr[k] = left[l]
                l += 1
            else:
                arr[k] = right[r]
                r += 1
            k += 1
            
        while l < len(left):
            arr[k] = left[l]
            k += 1
            l += 1
            
        while r < len(right):
            arr[k] = right[r]
            k += 1
            r += 1
            
arr = [9,8,7,6,5,4,300, 1]
mergeSort(arr)
print(arr)
        
        
        
        
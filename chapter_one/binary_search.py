

def binary_search(arr, element): 
    low = 0 
    high = len(arr) - 1

    while low <= high: 
        mid = (low + high) // 2 
        if arr[mid] < element : 
            low = mid + 1 
        elif arr[mid] > element  :
            high = mid - 1 
        else: 
            return mid
    return -1 
arr = [1,2,3,4]

print(binary_search(arr, 4))

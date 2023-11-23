
def find_smallest(arr): 
    smallest_index = 0
    for i in range(len(arr)): 
        if  arr[i] < arr[smallest_index] : 
            smallest_index = i
    
    return smallest_index


def selection_sort(arr): 
    new_arr = []
    for i in range(len(arr)): 
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

arr = [5,3,6,2,10]
print(selection_sort(arr))



## 
def selection_sort_v2(arr): 
    for i in range(len(arr)): 
        smallest_index = i
        for j in range(i, len(arr)): 
            if arr[j] < arr[smallest_index] :
                smallest_index = j
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr

arr = [5,3,6,2,10]
print(selection_sort_v2(arr))


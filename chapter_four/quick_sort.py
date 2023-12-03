

def quick_sort(arr): 
    if len(arr) < 2 :
        return arr 
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    grater = [i for i in arr[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(grater)



arr = [30, 50, -50, 10, 90 , 1000]
print(quick_sort(arr))




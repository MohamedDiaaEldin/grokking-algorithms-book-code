
import timeit

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

def selection_sort_v2(arr):
    for i in range(len(arr)):
        smallest_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr

# Assuming find_smallest is implemented somewhere

# Generate a random list for testing
import random

test_list = [random.randint(1, 1000) for _ in range(100)]

# Benchmark selection_sort
time_selection_sort = timeit.timeit(lambda: selection_sort(test_list.copy()), number=1000)

# Benchmark selection_sort_v2
time_selection_sort_v2 = timeit.timeit(lambda: selection_sort_v2(test_list.copy()), number=1000)

# print(f"Selection Sort Time: {time_selection_sort: .3f} seconds")
# print(f"Selection Sort v2 Time: {time_selection_sort_v2: .3f} seconds")


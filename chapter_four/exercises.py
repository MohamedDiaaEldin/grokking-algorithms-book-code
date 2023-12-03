


def sum(arr): 
    if len(arr) == 0 : 
        return 0
    return arr[0] + sum(arr[1:])




def count(arr): 
    if len(arr) == 0 :
        return 0 
    return 1 + count(arr[1:])

# print(count([]))
# print(count([1, 2]))
# print(count([1, 20, 30]))




def find_max_num(arr): 
    if len(arr) == 0 :
        return None
    if len(arr) == 2 : 
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub = find_max_num(arr[1:])
    return arr[0] if arr[0] > sub else sub



# print(find_max_num([]))
# print(find_max_num([1, 2]))
# print(find_max_num([1, 20, 30]))


def recursive_search(arr, low, high, target): 
    if high >= low : 
        mid  = (high + low) // 2 
        if arr[mid] == target :
            return mid
        elif arr[mid] > target: 
            return recursive_search(arr, low, mid-1, target)
        else:
            return recursive_search(arr, mid+1, high, target)            
    else:
        return -1 

def recursive_binary_search(arr, target): 
    return recursive_search(arr, 0, len(arr)-1, target)

# print(recursive_binary_search([], 1000))
# print(recursive_binary_search([1, 20, 30, 40], 1))
# print(recursive_binary_search([ -200, -50, 1, 30], 30) )
# print(recursive_binary_search([ -200, -50, 1, 30], -50) )
# print(recursive_binary_search([ -200, -50, 1, 30], -200) )

##### Quick Sort Ex. 

'''
EXERCISES
How long would each of these operations take in Big O notation?

4.5 Printing the value of each element in an array.  
= O(n)
4.6 Doubling the value of each element in an array.
= O(n)
4.7 Doubling the value of just the first element in an array.
O(1)
4.8 Creating a multiplication table with all the elements in the array. So
if your array is [2, 3, 7, 8, 10], you first multiply every element by 2,
then multiply every element by 3, then by 7, and so on.
o(n^2)
'''




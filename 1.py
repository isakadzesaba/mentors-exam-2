# Given an array containing n-1 numbers taken from the range 1 to n, write a function to find the missing number. There are no duplicates in the array.

# [1, 2, 4, 5] -> 3, [1] -> 2, [2, 3, 1, 5] -> 4



def find(arr):
    n = len(arr) + 1
    sum = n * (n + 1) // 2
    arr_1 = 0
    for i in arr:
        arr_1 += i
    return sum - arr_1

print(find([1, 2, 4, 5]))  
print(find([1]))           
print(find([2, 3, 1, 5]))
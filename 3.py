# Given an array of size n, find the majority element. The majority element is the element that appears more than n // 2 times. You may assume that the array is non-empty and the majority element always exists in the array.


# [3, 2, 3] -> 3, [2, 2, 1, 1, 2] -> 2, [1, 1, 1, 1, 1] -> 1


def majority(num):
    count = 0
    rame = None

    for i in num:
        if count == 0:
            rame = i
        count += 1 

        if num == rame:
            count += 1
        else:
            count -= 1
    
    return rame

print(majority([3, 2, 3]))
print(majority([2, 2, 1, 1, 2]))
print(majority([1, 1, 1, 1, 1]))
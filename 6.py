# Given two sorted arrays nums1 and nums2, return the mean of the two sorted arrays.

# [1, 2, 3], [4, 5, 6] -> 3.5,    [10, 20], [30, 40, 50] -> 30.0,    [-5, -3, -1], [1, 3, 5] -> 0.0

def sort_arr(num1, num2):
    rame = sorted(num1 + num2)
    sigrdze = len(rame)
    mean = float(0)

    if sigrdze > 0:
        mean = sum(rame) / sigrdze
    else:
        mean = 0.0

    return mean

print(sort_arr([1, 2, 3], [4, 5, 6]))         
print(sort_arr([10, 20], [30, 40, 50]))      
print(sort_arr([-5, -3, -1], [1, 3, 5]))      

"""
LeetCode 448: Find All Numbers Disappeared in an Array

Problem:
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.
"""

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    num_set = set(nums)
    res = []
    for i in range(1, len(nums) + 1):
        if i not in num_set:
            res.append(i)
    return res

    


# # Test cases
# print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1])) # Expected: [5, 6]
# print(find_disappeared_numbers([1, 1]))  # Expected: [2]




def find_disappeared_numbers2(nums: list[int]) -> list[int]:
    numset = set(nums)
    res = []
    for i in range(1,len(nums)+1):
        if i not in numset:
            res.append(i)
    return res

print(find_disappeared_numbers2([4, 3, 2, 7, 8, 2, 3, 1])) 

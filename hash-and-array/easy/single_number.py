"""
LeetCode 136: Single Number

Problem:
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.
"""

def single_number(nums: list[int]) -> int:
    res = set()
    for num in nums:
        if num not in res:
            res.add(num)
        else:
            res.remove(num)
    
    return res.pop()

# Test cases
print(single_number([2, 2, 1]))       # Expected: 1
print(single_number([4, 1, 2, 1, 2])) # Expected: 4
print(single_number([1]))             # Expected: 1

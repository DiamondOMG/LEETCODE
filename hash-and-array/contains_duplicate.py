"""
LeetCode 217: Contains Duplicate

Problem:
Given an integer array nums, return True if any value appears at least twice in the array,
and return False if every element is distinct.
"""

def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Test cases
print(contains_duplicate([1, 2, 3, 1]))       # Expected: True
print(contains_duplicate([1, 2, 3, 4]))       # Expected: False
print(contains_duplicate([1, 1, 1, 3, 3, 4])) # Expected: True

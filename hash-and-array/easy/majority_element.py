"""
LeetCode 169: Majority Element

Problem:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""

def majority_element(nums: list[int]) -> int:
    count_map = {}
    majority_threshold = len(nums) // 2  # เกินครึ่งหนึ่ง (n / 2)
    
    for num in nums:
        if num not in count_map:
            count_map[num] = 1
        else:
            count_map[num] += 1
            
        # ถ้าตัวไหนนับแล้วเกินครึ่ง ส่งคำตอบได้ทันที
        if count_map[num] > majority_threshold:
            return num
        
# Test cases
print(majority_element([3, 2, 3]))             # Expected: 3
print(majority_element([2, 2, 1, 1, 1, 2, 2])) # Expected: 2

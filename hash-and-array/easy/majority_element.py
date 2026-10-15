"""
LeetCode 169: Majority Element

Problem:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

โจทย์:
กำหนดอาร์เรย์ nums ที่มีสมาชิก n ตัว ให้หาตัวเลขที่ปรากฏมากกว่าครึ่งหนึ่งของอาร์เรย์
(มากกว่า ⌊n / 2⌋ ครั้ง) โดยรับประกันว่ามีตัวเลขดังกล่าวอยู่เสมอ
"""

def majority_element(nums: list[int]) -> int:
    show = {}
    threshold = len(nums)/2
    for i in range(len(nums)):
        if nums[i] not in show:
            show[nums[i]] = 1
        else:
            show[nums[i]] += 1
        if show[nums[i]] > threshold :
            return nums[i]
    return 0
        
# Test cases
print(majority_element([3, 2, 3]))             # Expected: 3
print(majority_element([2, 2, 1, 1, 1, 2, 2])) # Expected: 2
print(majority_element([1]))                    # Expected: 1
print(majority_element([4, 4, 2, 4, 3, 4, 4])) # Expected: 4

"""
LeetCode 349: Intersection of Two Arrays

Problem:
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

โจทย์:
กำหนดอาร์เรย์จำนวนเต็ม nums1 และ nums2 ให้คืนอาร์เรย์ของตัวเลขที่อยู่ในทั้งสองอาร์เรย์
ตัวเลขในคำตอบต้องไม่ซ้ำกัน และจะเรียงลำดับอย่างไรก็ได้
"""

def intersection_of_two_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1_set = set(nums1)
    nums2_set = set(nums2)

    return list(nums1_set & nums2_set)

# Test cases
print(intersection_of_two_arrays([1, 2, 2, 1], [2, 2]))       # Expected: [2]
print(intersection_of_two_arrays([4, 9, 5], [9, 4, 9, 8, 4])) # Expected: [9, 4] or [4, 9]
print(intersection_of_two_arrays([1, 2], [3, 4]))              # Expected: []
print(intersection_of_two_arrays([], [1]))                     # Expected: []
print(intersection_of_two_arrays([1, 1], [1]))                 # Expected: [1]

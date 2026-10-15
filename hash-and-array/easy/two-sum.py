"""
LeetCode 1: Two Sum

Problem:
Given an integer array nums and an integer target, return the indices of two numbers
such that they add up to target. You may not use the same element twice.
There is exactly one solution, and you may return the indices in any order.

โจทย์:
กำหนดอาร์เรย์จำนวนเต็ม nums และจำนวนเต็ม target ให้หาตำแหน่งของตัวเลข 2 ตัว
ที่บวกกันได้ target โดยห้ามใช้สมาชิกตำแหน่งเดียวกันซ้ำ
รับประกันว่ามีคำตอบเพียงหนึ่งคู่ และจะคืนตำแหน่งในลำดับใดก็ได้
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {nums[0]:0}
    for i in range(1,len(nums)):
        need = target-nums[i]

        if need in seen :
            return [i,seen[need]]
        seen[nums[i]] = i
    return []


print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))
print(twoSum([0, 4, 3, 0], 0)) # Expected: [3, 0] or [0, 3]

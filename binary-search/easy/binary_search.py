"""LeetCode 704: Binary Search | ค้นหาแบบ Binary Search

Problem (EN): Given a sorted integer array nums and an integer target, return
its index if found; otherwise return -1. Use O(log n) time.
โจทย์ (TH): รับอาร์เรย์จำนวนเต็ม nums ที่เรียงแล้วและ target คืน index
เมื่อพบ มิฉะนั้นคืน -1 โดยใช้เวลา O(log n)

Examples / ตัวอย่าง:
1) nums=[-1,0,3,5,9,12], target=9 -> 4
2) nums=[-1,0,3,5,9,12], target=2 -> -1
3) nums=[5], target=5 -> 0
4) nums=[], target=0 -> -1
"""


def search(nums: list[int], target: int) -> int:
    pass


print(search([-1, 0, 3, 5, 9, 12], 9))  # 4
print(search([-1, 0, 3, 5, 9, 12], 2))  # -1
print(search([5], 5))                    # 0
print(search([], 0))                      # -1

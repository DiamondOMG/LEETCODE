"""LeetCode 26: Remove Duplicates from Sorted Array | ลบค่าซ้ำในอาร์เรย์เรียงแล้ว

Problem (EN): Remove duplicates in-place from sorted nums. Return k, the
number of unique values; the first k positions must contain those values.
โจทย์ (TH): ลบค่าซ้ำจาก nums ที่เรียงแล้วแบบ in-place คืน k ซึ่งเป็นจำนวน
ค่าที่ไม่ซ้ำ และสมาชิก k ตัวแรกต้องเป็นค่าที่ไม่ซ้ำ

Examples / ตัวอย่าง:
1) [1,1,2] -> k=2, prefix=[1,2]
2) [0,0,1,1,1,2,2,3,3,4] -> k=5, prefix=[0,1,2,3,4]
3) [1] -> k=1, prefix=[1]
4) [] -> k=0, prefix=[]
"""


def remove_duplicates(nums: list[int]) -> int:
    pass


nums = [1, 1, 2]
print(remove_duplicates(nums), nums)  # 2, prefix [1, 2]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(remove_duplicates(nums), nums)  # 5, prefix [0, 1, 2, 3, 4]
nums = [1]
print(remove_duplicates(nums), nums)  # 1, prefix [1]
nums = []
print(remove_duplicates(nums), nums)  # 0, prefix []

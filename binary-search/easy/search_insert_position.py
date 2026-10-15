"""LeetCode 35: Search Insert Position | ค้นหาตำแหน่งแทรก

Problem (EN): Given a sorted array and target, return its index if found,
or the index where it should be inserted to keep the array sorted.
โจทย์ (TH): รับอาร์เรย์ที่เรียงแล้วและ target คืน index ถ้าพบ
ถ้าไม่พบให้คืนตำแหน่งที่ควรแทรกเพื่อให้อาร์เรย์ยังเรียงอยู่

Examples / ตัวอย่าง:
1) [1,3,5,6], target=5 -> 2
2) [1,3,5,6], target=2 -> 1
3) [1,3,5,6], target=7 -> 4
4) [1], target=0 -> 0
"""


def search_insert(nums: list[int], target: int) -> int:
    pass


print(search_insert([1, 3, 5, 6], 5))  # 2
print(search_insert([1, 3, 5, 6], 2))  # 1
print(search_insert([1, 3, 5, 6], 7))  # 4
print(search_insert([1], 0))            # 0

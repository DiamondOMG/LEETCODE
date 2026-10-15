"""LeetCode 1046: Last Stone Weight | น้ำหนักหินก้อนสุดท้าย

Problem (EN): Repeatedly smash the two heaviest stones. Equal stones are both
removed; otherwise the difference remains. Return the last stone's weight,
or 0 if none remain.
โจทย์ (TH): เลือกหินหนักที่สุดสองก้อนมาชนกัน ถ้าน้ำหนักเท่ากันจะหายไปทั้งคู่
ถ้าไม่เท่ากันจะเหลือผลต่าง คืนค่าน้ำหนักก้อนสุดท้าย หรือ 0 ถ้าไม่เหลือ

Examples / ตัวอย่าง:
1) [2,7,4,1,8,1] -> 1
2) [1] -> 1
3) [3,3] -> 0
4) [2,2,2,2] -> 0
"""


def last_stone_weight(stones: list[int]) -> int:
    pass


print(last_stone_weight([2, 7, 4, 1, 8, 1]))  # 1
print(last_stone_weight([1]))                 # 1
print(last_stone_weight([3, 3]))              # 0
print(last_stone_weight([2, 2, 2, 2]))        # 0

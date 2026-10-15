"""LeetCode 278: First Bad Version | เวอร์ชันเสียตัวแรก

Problem (EN): Versions 1..n are good until the first bad version; every later
version is bad. Find the first bad version using isBadVersion(version).
โจทย์ (TH): เวอร์ชัน 1 ถึง n จะเสียตั้งแต่เวอร์ชันแรกที่เสียเป็นต้นไป
หาเวอร์ชันเสียตัวแรก โดยใช้ API isBadVersion(version) ของ LeetCode

Examples / ตัวอย่าง (bad version -> answer):
1) n=5, first bad=4 -> 4
2) n=1, first bad=1 -> 1
3) n=10, first bad=7 -> 7
4) n=2, first bad=2 -> 2
"""


def first_bad_version(n: int) -> int:
    # LeetCode provides isBadVersion(version).
    pass


# Examples are comments because isBadVersion is provided by LeetCode.
# print(first_bad_version(5))   # 4 when first bad version is 4
# print(first_bad_version(1))   # 1
# print(first_bad_version(10))  # 7 when first bad version is 7
# print(first_bad_version(2))   # 2 when first bad version is 2

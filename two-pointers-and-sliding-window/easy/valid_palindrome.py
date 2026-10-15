"""LeetCode 125: Valid Palindrome | ตรวจสอบพาลินโดรม

Problem (EN): Return True if s is a palindrome, considering only
alphanumeric characters and ignoring letter case.
โจทย์ (TH): คืน True ถ้า s อ่านกลับหน้า-หลังเหมือนกัน โดยพิจารณาเฉพาะ
ตัวอักษรและตัวเลข และไม่สนตัวพิมพ์เล็ก/ใหญ่

Examples / ตัวอย่าง:
1) "A man, a plan, a canal: Panama" -> True
2) "race a car" -> False
3) " " -> True
4) "0P" -> False
"""


def is_palindrome(s: str) -> bool:
    pass


print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                      # False
print(is_palindrome(" "))                                # True
print(is_palindrome("0P"))                               # False

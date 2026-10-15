"""
LeetCode 383: Ransom Note

Problem:
Given two strings ransom_note and magazine, return True if ransom_note can be
constructed by using the letters from magazine and False otherwise.

Each letter in magazine can only be used once.

โจทย์:
กำหนดสตริง ransom_note และ magazine ให้ตรวจสอบว่าเราสามารถสร้าง ransom_note
โดยใช้ตัวอักษรจาก magazine ได้หรือไม่

ตัวอักษรแต่ละตัวใน magazine ใช้ได้เพียงครั้งเดียว
"""


def can_construct(ransom_note: str, magazine: str) -> bool:
    for rs in range(len(ransom_note)):
        if ransom_note[rs] in magazine:    
            magazine = magazine.replace(ransom_note[rs],"",1)
        else :
            return False
    return True


# Test cases
print(can_construct("a", "b"))          # Expected: False
print(can_construct("aa", "ab"))        # Expected: False
print(can_construct("aa", "aab"))       # Expected: True
print(can_construct("", "abc"))           # Expected: True

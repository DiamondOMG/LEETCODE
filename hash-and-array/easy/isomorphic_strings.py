"""
LeetCode 205: Isomorphic Strings

Problem:
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

โจทย์:
กำหนดสตริง s และ t ให้ตรวจสอบว่าทั้งสองเป็นสตริงแบบไอโซมอร์ฟิกหรือไม่
กล่าวคือ สามารถแทนที่ตัวอักษรใน s เพื่อให้ได้ t โดยตัวอักษรเดียวกันต้องถูกแทนที่
ด้วยตัวอักษรเดียวกันทุกตำแหน่ง และยังคงลำดับเดิมไว้
ตัวอักษรต่างกันห้ามแทนที่ด้วยตัวอักษรเดียวกัน แต่สามารถแทนที่ด้วยตัวเองได้
"""

def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_iso = {}
    t_iso = {}
    for i in range(len(s)):
        if s[i] in s_iso and s_iso[s[i]] != t[i]:
            return False
        if t[i] in t_iso and t_iso[t[i]] != s[i]:
            return False
        s_iso[s[i]] = t[i]
        t_iso[t[i]] = s[i]

    return True
# Test cases
print(is_isomorphic("egg", "add"))     # Expected: True
print(is_isomorphic("foo", "bar"))     # Expected: False
print(is_isomorphic("paper", "title")) # Expected: True
print(is_isomorphic("ab", "aa"))       # Expected: False

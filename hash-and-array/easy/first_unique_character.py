"""
LeetCode 387: First Unique Character in a String

Problem:
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

โจทย์:
กำหนดสตริง s ให้หาตัวอักษรตัวแรกที่ปรากฏเพียงครั้งเดียว แล้วคืนตำแหน่งของตัวอักษรนั้น
หากไม่มี ให้คืนค่า -1
"""

def first_unique_character(s: str) -> int:
    char_count = {}
    
    # 1. นับความถี่ของตัวอักษรแต่ละตัว
    for ch in s:
        if ch not in char_count:
            char_count[ch] = 1
        else:
            char_count[ch] += 1
        
    # 2. วนลูปหาตัวแรกที่ความถี่เป็น 1
    for i in range(len(s)):
        ch = s[i]
        if char_count[ch] == 1:
            return i
            
    return -1

# Test cases
# print(first_unique_character("leetcode"))     # Expected: 0
# print(first_unique_character("loveleetcode")) # Expected: 2
# print(first_unique_character("aabb"))         # Expected: -1

def first_unique_character2 (s : str)-> int:
    ch={}
    for i in s:
        if i not in ch:
            ch[i] = 1
        else:
            ch[i] +=1
    
    for i in range(len(s)):
        c = s[i]
        if ch[c] == 1:
            return i
    return -1

print(first_unique_character2("leetcode"))     # Expected: 0
print(first_unique_character2("loveleetcode")) # Expected: 2
print(first_unique_character2("aabb"))         # Expected: -1
print(first_unique_character2("z"))             # Expected: 0    
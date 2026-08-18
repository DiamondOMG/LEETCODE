"""
LeetCode 387: First Unique Character in a String

Problem:
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.
"""

def first_unique_character(s: str) -> int:
    char_count = {}
    
    # 1. นับความถี่ของตัวอักษรแต่ละตัว
    for ch in s:
        char_count[ch] = char_count.get(ch, 0) + 1
        
    # 2. วนลูปหาตัวแรกที่ความถี่เป็น 1
    for i, ch in enumerate(s):
        if char_count[ch] == 1:
            return i
            
    return -1

# Test cases
print(first_unique_character("leetcode"))     # Expected: 0
print(first_unique_character("loveleetcode")) # Expected: 2
print(first_unique_character("aabb"))         # Expected: -1

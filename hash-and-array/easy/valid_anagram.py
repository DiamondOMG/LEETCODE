"""
LeetCode 242: Valid Anagram

Problem:
Given two strings s and t, return True if t is an anagram of s, and False otherwise.
(An Anagram is a word formed by rearranging the letters of a different word,
using all the original letters exactly once).
"""

def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_ana = {}
    t_ana = {}
    for i in s:
        if i not in s_ana:
            s_ana[i] = 1
        else:
            s_ana[i] +=1

    for i in t:
        if i not in t_ana:
            t_ana[i] = 1
        else:
            t_ana[i] +=1

    if s_ana == t_ana:
        return True
    else:
        return False
    

# Test cases
print(valid_anagram("anagram", "nagaram")) # Expected: True
print(valid_anagram("rat", "car"))         # Expected: False

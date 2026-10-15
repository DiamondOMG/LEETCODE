"""
LeetCode 242: Valid Anagram

Problem:
Given two strings s and t, return True if t is an anagram of s, and False otherwise.
(An Anagram is a word formed by rearranging the letters of a different word,
using all the original letters exactly once).

โจทย์:
กำหนดสตริง s และ t ให้คืนค่า True หาก t เป็นแอนนาแกรมของ s มิฉะนั้นคืนค่า False
แอนนาแกรมคือการนำตัวอักษรทั้งหมดของคำเดิมมาเรียงใหม่ โดยใช้แต่ละตัวตามจำนวนครั้งเดิม
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
    return s_ana == t_ana

    

# Test cases
print(valid_anagram("anagram", "nagaram")) # Expected: True
print(valid_anagram("rat", "car"))         # Expected: False
print(valid_anagram("", ""))                # Expected: True
print(valid_anagram("a", "ab"))             # Expected: False


def valid_anagram2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_ana = {}
    t_ana = {}

    for i in s:
        if i not in s_ana:
            s_ana[i] = 1
        else :
            s_ana[i] += 1

    for i in t:
        if i not in t_ana:
            t_ana[i] = 1
        else :
            t_ana[i] += 1

    return t_ana == s_ana

print(valid_anagram2("anagram", "nagaram")) # Expected: True
print(valid_anagram2("rat", "car"))         # Expected: False
        
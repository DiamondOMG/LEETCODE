"""LeetCode 20: Valid Parentheses | วงเล็บถูกต้อง

Problem (EN): Determine whether brackets (), [], and {} are closed in the
correct order and each opening bracket has a matching closing bracket.
โจทย์ (TH): ตรวจว่าวงเล็บ (), [] และ {} เปิด-ปิดครบและเรียงลำดับถูกต้องหรือไม่

Examples / ตัวอย่าง:
1) "()" -> True
2) "()[]{}" -> True
3) "(]" -> False
4) "([)]" -> False
"""


def is_valid(s):
    pairs = { "(":")","{":"}","[":"]"}
    stack = []
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char :
                return False 
    return not stack
		 


print(is_valid("()"))      # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))      # False
print(is_valid("([)]"))    # False

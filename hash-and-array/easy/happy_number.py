"""
LeetCode 202: Happy Number

Problem:
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares
  of its digits.
- Repeat the process until the number equals 1, or it loops endlessly in a cycle
  that does not include 1.
- Those numbers for which this process ends in 1 are happy.

โจทย์:
เขียนอัลกอริทึมตรวจสอบว่าเลข n เป็นเลข Happy หรือไม่

เลข Happy คือเลขที่ทำตามขั้นตอนต่อไปนี้:
- เริ่มจากจำนวนเต็มบวก แล้วแทนที่ด้วยผลรวมกำลังสองของเลขแต่ละหลัก
- ทำซ้ำจนกว่าจะได้เลข 1 หรือวนซ้ำเป็นวงจรที่ไม่มีเลข 1
- ถ้ากระบวนการจบลงที่เลข 1 แสดงว่าเป็นเลข Happy
"""


def is_happy(n: int) -> bool:
    c = n
    repeat = set()
    while (1):
        happy = [int (x) for x in str(c)]
        sum = 0
        for num in happy:
            sum += num*num
        if sum == 1:
            return True
        if sum in repeat:
            return False
        repeat.add(sum)
        c = sum


# Test cases
print(is_happy(19))  # Expected: True
print(is_happy(2))   # Expected: False
print(is_happy(1))   # Expected: True
print(is_happy(7))   # Expected: True
print(is_happy(4))   # Expected: False

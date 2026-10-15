"""LeetCode 682: Baseball Game | คำนวณคะแนนเบสบอล

Problem (EN): Process operations: an integer adds a score, '+' adds the last
two scores, 'D' doubles the last score, and 'C' removes the last score.
Return the total score.
โจทย์ (TH): คำนวณ operations: ตัวเลขเพิ่มคะแนน, '+' บวกสองคะแนนล่าสุด,
'D' คูณสองคะแนนล่าสุด และ 'C' ยกเลิกคะแนนล่าสุด คืนผลรวมคะแนน

Examples / ตัวอย่าง:
1) ["5","2","C","D","+"] -> 30
2) ["5","-2","4","C","D","9","+","+"] -> 27
3) ["1"] -> 1
4) ["1","D"] -> 3
"""


def cal_points(operations: list[str]) -> int:
    pass


print(cal_points(["5", "2", "C", "D", "+"]))                 # 30
print(cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # 27
print(cal_points(["1"]))                                         # 1
print(cal_points(["1", "D"]))                                   # 3

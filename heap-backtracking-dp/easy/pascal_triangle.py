"""LeetCode 118: Pascal's Triangle | สามเหลี่ยมปาสกาล

Problem (EN): Given numRows, generate the first numRows of Pascal's triangle.
Each number is the sum of the two numbers directly above it.
โจทย์ (TH): รับ numRows สร้างสามเหลี่ยมปาสกาล numRows แถว
ตัวเลขแต่ละช่องเป็นผลรวมของสองช่องที่อยู่เหนือขึ้นไป

Examples / ตัวอย่าง:
1) 1 -> [[1]]
2) 2 -> [[1],[1,1]]
3) 3 -> [[1],[1,1],[1,2,1]]
4) 5 -> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""


def generate(num_rows: int) -> list[list[int]]:
    pass


print(generate(1))  # [[1]]
print(generate(2))  # [[1], [1, 1]]
print(generate(3))  # [[1], [1, 1], [1, 2, 1]]
print(generate(5))  # first five rows

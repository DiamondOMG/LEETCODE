"""LeetCode 121: Best Time to Buy and Sell Stock | ซื้อขายหุ้นกำไรสูงสุด

Problem (EN): Given prices by day, choose one day to buy and a later day to
sell. Return the maximum profit, or 0 if no profit is possible.
โจทย์ (TH): รับราคาหุ้นรายวัน เลือกซื้อก่อนขายเพื่อให้กำไรสูงสุด
คืนกำไรสูงสุด หรือ 0 ถ้าไม่มีกำไร

Examples / ตัวอย่าง:
1) [7,1,5,3,6,4] -> 5
2) [7,6,4,3,1] -> 0
3) [2,4,1] -> 2
4) [1] -> 0
"""


def max_profit(prices: list[int]) -> int:
    pass


print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
print(max_profit([7, 6, 4, 3, 1]))     # 0
print(max_profit([2, 4, 1]))           # 2
print(max_profit([1]))                 # 0

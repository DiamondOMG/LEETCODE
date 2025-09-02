def maxProfit(prices: list[int]) -> int:
    profit=0
    for i in range(len(prices)):
        for j in range(i,len(prices)):
            check=prices[j]-prices[i]
            if check > profit:
                profit = check

    return profit

def maxProfit2(prices: list[int]) -> int:
    min_price = float('inf')
    profit = 0
    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        profit = max(profit, prices[i] - min_price)
    return profit


print(maxProfit2([7,1,5,3,6,4]))
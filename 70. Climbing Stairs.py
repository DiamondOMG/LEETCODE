import math

class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        return round((phi**(n+1) - psi**(n+1)) / sqrt5)

def climbStairs( n: int) -> int:
    if n == 2 :
        return 2
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

def climbStairs2( n: int) -> int:
    if n==2:
        return 2
    dp = [0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

print(climbStairs(7))
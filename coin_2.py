# problem: given coin array & amount integer to find
# how many combinations using the coins make up the integer
# assummed you have infinet number of coins
from black import List


def change(amount: int, coins: List[int]) -> int:
    # 2 dimensional for dp cache
    # 0(n * m)
    dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
    dp[0] = [1] * (len(coins) + 1)

    for a in range(1, amount + 1):
        for i in range(len(coins) - 1, -1, -1):
            dp[a][i] = dp[a][i + 1]
            if a - coins[i] >= 0:
                dp[a][i] += dp[a - coins[i]][i]
    return dp[amount][0]


print(change(5, [1, 2, 5]))

# Simple solution that I cant visualise

# cache = {}

# def dfs(i, a):
#     if a == amount:
#         return 1
#         # base case amount
#     if a > amount:
#         return 0
#         if i == len(coins):
#             return 0
#             # out of bounds gone into -
#         if (i, a) in cache:
#             return cache[(i, a)]

#         cache[(i, a)] = dfs(i, a + coins[i] + dfs(i + 1, a))
#         return cache[(i, a)]

#     return dfs(0, 0)

# LINK for explanation
# https://www.youtube.com/watch?v=Mjy4hd2xgrs

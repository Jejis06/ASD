'''
Klasyczny dyskretny problem plecakowy 

[ O(n * b) ]
'''

def knapsack(price:list[int], weight:list[int], B:int) -> int:
    n = len(price)
    dp = [[0 for _ in range(B + 1)] for _ in range(n)]

    for b in range(weight[0], B+1):
        dp[0][b] = price[0]

    for i in range(1, n):
        for b in range(B + 1):
            dp[i][b] = dp[i-1][b]
            if b >= weight[i]:
                dp[i][b] = max(dp[i][b], dp[i-1][b - weight[i]] + price[i])

    return dp[n-1][B]

def smart_knapsack(price:list[int], weight:list[int], B:int) -> int:
    n = len(price)

    dp = [0] * (B + 1)
    for i in range(n):
        for b in range(B, weight[i] - 1, -1):
            dp[b] = max(dp[b], dp[b - weight[i]] + price[i])

    return dp[B]


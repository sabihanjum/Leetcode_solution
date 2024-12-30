"""Given an array of coins[] of size n and a target value sum, where coins[i] represent the coins of different denominations. You have an infinite supply of each of the coins. The task is to find the minimum number of coins required to make the given value sum. If it’s not possible to make a change, return -1."""
def minCoins(coins, sum):
    dp = [float('inf')] * (sum + 1)
    dp[0] = 0

    for i in range(len(coins) - 1, -1, -1):
        for j in range(1, sum + 1):
            take = float('inf')
            noTake = float('inf')

            # If we take coins[i] coin
            if j - coins[i] >= 0 and coins[i] > 0:
                take = dp[j - coins[i]]
                if take != float('inf'):
                    take += 1

            if i + 1 < len(coins):
                noTake = dp[j]

            dp[j] = min(take, noTake)

    return dp[sum] if dp[sum] != float('inf') else -1


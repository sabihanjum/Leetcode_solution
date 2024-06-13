from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array where dp[i] represents the minimum number of coins needed to make amount i
        # Use float('inf') to represent that the amount is initially unreachable
        dp = [float('inf') for _ in range(amount+1)]
        
        # Base case: 0 coins are needed to make amount 0
        dp[0] = 0

        # Fill the dp array
        for i in range(len(dp)):
            for c in coins:
                if i - c >= 0:  # Ensure we do not go out of bounds
                    # Update dp[i] with the minimum coins needed
                    dp[i] = min(dp[i], dp[i - c] + 1)

        # If dp[-1] is still float('inf'), it means the amount cannot be made up by any combination of the coins
        return -1 if dp[-1] == float('inf') else dp[-1]

# Example usage
# solution = Solution()
# print(solution.coinChange([1, 2, 5], 11))  # Output: 3 (11 = 5 + 5 + 1)
# print(solution.coinChange([2], 3))  # Output: -1 (3 cannot be formed using only coin of denomination 2)

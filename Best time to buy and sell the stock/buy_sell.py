class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price as positive infinity
        min_price = float('inf')
        # Initialize the maximum profit as 0
        max_profit = 0
        # Iterate through each price in the list
        for i in prices:
            # If the current price is lower than the minimum price seen so far
            if min_price > i:
                # Update the minimum price to the current price
                min_price = i
            # If the current price allows for a higher profit than seen before
            else:
                # Update the maximum profit if a higher profit is achievable
                max_profit = max(max_profit, i-min_price)
        # Return the maximum profit
        return max_profit

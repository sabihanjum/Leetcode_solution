"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

class Solution:
    def maxProfit(self, arr):
        # Initialize maxPro to store the maximum profit found, starting at 0
        maxPro = 0
        
        # Initialize minPrice to store the minimum price encountered so far, starting at infinity
        minPrice = float('inf')

        # Iterate through the array to process each price
        for i in range(len(arr)):
            # Update minPrice to the smallest price encountered so far
            minPrice = min(minPrice, arr[i])
            
            # Calculate the potential profit if we bought at minPrice and sold at the current price
            # Update maxPro if this potential profit is greater than the previously recorded maximum profit
            maxPro = max(maxPro, arr[i] - minPrice)
        
        # Return the maximum profit found
        return maxPro

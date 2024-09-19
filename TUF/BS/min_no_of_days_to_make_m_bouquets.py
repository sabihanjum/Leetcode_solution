"""You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1."""

from typing import List

class Solution:
    
    # Helper function to check if it's possible to make 'm' bouquets by a given 'day'
    def possible(self, bloomDay: List[int], day: int, m: int, k: int) -> bool:
        n = len(bloomDay)  # size of the array
        cnt = 0  # count of consecutive flowers that can be picked
        bouquets = 0  # number of bouquets made so far

        # Loop through the bloomDay array
        for i in range(n):
            if bloomDay[i] <= day:
                cnt += 1  # Flower can bloom by 'day', increment the count
            else:
                bouquets += cnt // k  # Make bouquets from consecutive flowers
                cnt = 0  # Reset count if flowers are not blooming by 'day'
        
        # Add any remaining bouquets from the last segment
        bouquets += cnt // k
        
        # Check if the required number of bouquets can be made
        return bouquets >= m

    # Main function to find the minimum number of days to make 'm' bouquets
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        totalFlowersNeeded = m * k  # Total number of flowers needed

        # If total flowers required exceed the number of flowers available, it's impossible
        if totalFlowersNeeded > len(bloomDay):
            return -1

        # Initialize binary search on the minimum and maximum possible day
        low, high = min(bloomDay), max(bloomDay)

        # Binary search for the minimum day to achieve 'm' bouquets
        while low <= high:
            mid = (low + high) // 2

            # If it's possible to make 'm' bouquets by 'mid' day, try earlier days
            if self.possible(bloomDay, mid, m, k):
                high = mid - 1
            else:
                low = mid + 1  # Otherwise, try later days

        # 'low' is the minimum valid day where we can make 'm' bouquets
        return low

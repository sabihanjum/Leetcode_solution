"""A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days."""


class Solution:
    def findDays(self, weights, cap):  # Added 'self' as the first parameter
        days = 1
        load = 0
        n = len(weights)
        
        for i in range(n):
            if load + weights[i] > cap:
                days += 1
                load = weights[i]  # Move to the next day, starting with the current weight
            else:
                load += weights[i]  # Accumulate the load
        
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)  # The minimum capacity should be at least the max weight
        high = sum(weights)  # The maximum capacity could be the total sum of weights
        
        while low <= high:
            mid = (low + high) // 2
            numberOfDays = self.findDays(weights, mid)  # Call findDays with 'self'

            if numberOfDays <= days:  # Use 'days' instead of undefined 'd'
                high = mid - 1  # Try to find a smaller feasible capacity
            else:
                low = mid + 1  # Increase capacity to meet the requirement
        
        return low  # Return the minimum feasible capacity

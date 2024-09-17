"""Given an integer n, find the square root of n. If n is not a perfect square, then return the floor value.

Floor value of any number is the greatest Integer which is less than or equal to that number"""

class Solution:
    def floorSqrt(self, n): 
        # Initialize the lower bound (low) to 1 and upper bound (high) to n
        low = 1
        high = n
        
        # Binary search to find the largest integer whose square is <= n
        while low <= high:
            # Find the mid-point between low and high
            mid = (low + high) // 2
            # Compute the square of the mid-point value
            val = mid * mid
            
            # If the square of mid is less than or equal to n,
            # we update low to search the right half
            if val <= n:
                low = mid + 1
            # If the square of mid is greater than n, we search the left half
            else:
                high = mid - 1
        
        # Return the value of high, which will be the floor of the square root of n
        return high

"""You are given a number n. Find the total count of set bits for all numbers from 1 to n (both inclusive)"""

class Solution:
    # Function to return the sum of count of set bits in the integers from 1 to n
    def countSetBits(self, n):
        # Increment n by 1 to account for the range [1, n] inclusive
        n += 1
        
        # Initialize the total count of set bits
        count = 0
        
        # Start with x = 2 (to consider bit positions starting from the least significant bit)
        x = 2
        
        # Continue until x/2 (shifted right by 1) is less than n
        while (x >> 1) < n:
            # Calculate how many complete groups of 'x' exist in the range [0, n-1]
            quotient = n // x
            
            # Add the total number of set bits contributed by the complete groups
            # Each group contributes (x / 2) set bits
            count += quotient * (x >> 1)
            
            # Calculate the remainder of numbers that don't form a complete group
            remainder = n % x
            
            # If the remainder exceeds half of the group size (x / 2),
            # additional set bits are contributed by these numbers
            if remainder > (x >> 1):
                count += remainder - (x >> 1)
            
            # Move to the next bit position (double x)
            x *= 2
        
        # Return the total count of set bits in the range [1, n]
        return count

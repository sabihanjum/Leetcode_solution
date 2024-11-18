"""A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.

For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal."""

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Initialize a counter to keep track of the number of bit flips required
        count = 0
        
        # XOR the start and goal to identify differing bits
        # The XOR result will have 1s in the positions where start and goal differ
        xor = start ^ goal
        
        # Count the number of 1s in the XOR result, as each 1 represents a bit flip needed
        while xor:
            # Increment the counter for each differing bit (1 in the XOR result)
            count += 1
            
            # Use the operation `xor & (xor - 1)` to remove the least significant 1 from xor
            # This reduces the number of 1s in the XOR result, progressing the loop
            xor &= xor - 1
        
        # Return the total count of differing bits, i.e., the minimum bit flips needed
        return count

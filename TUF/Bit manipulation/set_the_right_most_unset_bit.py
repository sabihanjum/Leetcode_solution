"""Given a non-negative number n . The problem is to set the rightmost unset bit in the binary representation of n."""

class Solution:
    def setBit(self, n):
        # Function to set the first unset (0) bit to 1 in the binary representation of n
        
        # Initialize position to track the bit index (starting from 0)
        pos = 0
        
        # Copy of n to manipulate and check individual bits
        k = n
        
        # Loop to find the first unset bit (0)
        while k & 1 != 0:  # Check if the least significant bit (LSB) is 1
            k = k >> 1     # Right shift to move to the next bit
            pos += 1       # Increment the bit position
        
        # Use bitwise OR to set the first unset bit (0) to 1
        # (1 << pos) creates a number with only the bit at position `pos` set to 1
        return n | (1 << pos)

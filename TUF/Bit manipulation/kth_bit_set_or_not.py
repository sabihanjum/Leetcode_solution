"""Given a number n and a bit number k, check if the kth index bit of n is set or not. A bit is called set if it
is 1. The position of set bit '1' should be indexed starting with 0 from the LSB side in the binary representation 
of the number.
Note: Index is starting from 0. You just need to return true or false."""

class Solution:
    
    # Function to check if the K-th bit is set (1) or not (0).
    # Parameters:
    # n: The number in which to check the K-th bit.
    # k: The 0-based index of the bit to check.
    def checkKthBit(self, n, k):
        # Right shift the number `n` by `k` positions.
        # This brings the K-th bit to the least significant bit (LSB) position.
        # Perform a bitwise AND operation with 1 to isolate the LSB.
        # If the result is 1, the K-th bit is set; otherwise, it's not.
        return (n >> k) & 1

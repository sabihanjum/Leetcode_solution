"""Given a 32 bit unsigned integer num and an integer i. Perform following operations on the number - 
1. Get ith bit
2. Set ith bit
3. Clear ith bit

Note : For better understanding, we are starting bits from 1 instead 0. (1-based). You have to print space three
space seperated values ( as shown in output without a line break) and do not have to return anything."""

class Solution:
    def bitManipulation(self, n, i):
        # Function to perform bit manipulation on a given number `n`
        # and bit position `i`. The function determines if the `i-th`
        # bit is set, sets the `i-th` bit, and clears the `i-th` bit.

        # Check if the i-th bit is set (1 or 0)
        # (1 << (i-1)) creates a mask where only the i-th bit is set.
        # `n & (1 << (i-1))` checks if the i-th bit in `n` is 1.
        if n & (1 << (i-1)):
            x = 1  # i-th bit is set (1)
        else:
            x = 0  # i-th bit is not set (0)

        # Print whether the i-th bit is set
        print(x, end=" ")

        # Set the i-th bit in `n` (make it 1)
        # `n | (1 << (i-1))` ensures the i-th bit is set, leaving other bits unchanged.
        print(n | (1 << (i-1)), end=" ")

        # Clear the i-th bit in `n` (make it 0)
        # `~(1 << (i-1))` creates a mask where only the i-th bit is cleared.
        # `n & (~(1 << (i-1)))` clears the i-th bit, leaving other bits unchanged.
        print(n & (~(1 << (i-1))))

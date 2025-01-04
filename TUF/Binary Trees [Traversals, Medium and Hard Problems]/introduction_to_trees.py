"""Given an integer i. Print the maximum number of nodes on level i of a binary tree."""

class Solution:
    def countNodes(self, i):
        # Assign input value to a variable for clarity
        n = i

        # Handle edge case: If the input is 0, return -1 as an invalid result
        if n == 0: 
            return -1

        # Handle edge case: If the input is 1, return 1 as there's only one node
        if n == 1: 
            return 1

        # Calculate 2 raised to the power of n
        x = 2**n

        # Calculate half of x
        y = x // 2

        # Check if y is even
        if y % 2 == 0:
            # If y is even, return it as the result
            return y
        else:
            # If y is odd, return y-1 to ensure an even number
            return y - 1

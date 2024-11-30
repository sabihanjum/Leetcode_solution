"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining."""

class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Calculate the amount of water that can be trapped between the bars.

        Args:
        height: List[int] - A list representing the height of bars.

        Returns:
        int - The total amount of water trapped.
        """
        n = len(height)  # Total number of bars
        if n == 0:  # If there are no bars, no water can be trapped
            return 0

        # Arrays to store the maximum heights from the left and right
        l = [0] * n  # l[i] will store the maximum height from index 0 to i
        r = [0] * n  # r[i] will store the maximum height from index i to n-1

        # Build the 'l' array
        for i, h in enumerate(height):
            l[i] = h if i == 0 else max(h, l[i - 1])
            # At each position, calculate the maximum height seen so far from the left

        # Build the 'r' array (from right to left)
        for i, h in reversed(list(enumerate(height))):
            r[i] = h if i == n - 1 else max(h, r[i + 1])
            # At each position, calculate the maximum height seen so far from the right

        # Calculate the total water trapped
        return sum(
            min(l[i], r[i]) - h  # Water level is limited by the shorter of the two max heights
            for i, h in enumerate(height)
        )

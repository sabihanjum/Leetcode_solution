"""Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram."""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Calculates the largest rectangular area in a histogram.

        Args:
        heights (List[int]): A list of integers representing the heights of histogram bars.

        Returns:
        int: The maximum area of the rectangle that can be formed.
        """
        maxArea = 0  # Variable to keep track of the maximum area
        stack = []  # Monotonic stack to store pairs of (index, height)

        # Iterate through each bar in the histogram
        for i, h in enumerate(heights):
            start = i  # The initial position where the current height can extend
            # While the current height is less than the height at the top of the stack,
            # calculate the area for the popped height as the shortest bar in the rectangle
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))  # Calculate the area
                start = index  # Update the starting position for the current height
            # Push the current height along with its start index onto the stack
            stack.append((start, h))
        
        # Process any remaining heights in the stack
        for i, h in stack:
            # Calculate area for bars in the stack using the width till the end of the histogram
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea  # Return the maximum area

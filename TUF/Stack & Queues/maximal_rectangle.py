"""Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area."""

class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        """
        Calculates the area of the largest rectangle containing only '1's in a binary matrix.

        Args:
        matrix (list[list[str]]): 2D binary matrix with '0' and '1' as elements.

        Returns:
        int: The area of the largest rectangle.
        """
        if not matrix:  # If the matrix is empty, return 0
            return 0

        ans = 0  # Variable to store the maximum rectangle area
        hist = [0] * len(matrix[0])  # Initialize a histogram for the first row

        def largestRectangleArea(heights: list[int]) -> int:
            """
            Helper function to calculate the largest rectangle area in a histogram.

            Args:
            heights (list[int]): List of heights representing the histogram.

            Returns:
            int: The largest rectangle area in the histogram.
            """
            ans = 0
            stack = []  # Monotonic stack to store indices of heights

            # Iterate through heights, including a sentinel value at the end
            for i in range(len(heights) + 1):
                # While the current height is less than the height at the top of the stack
                while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
                    h = heights[stack.pop()]  # Height of the popped bar
                    # Calculate the width using the index difference
                    w = i - stack[-1] - 1 if stack else i
                    ans = max(ans, h * w)  # Update the maximum area
                stack.append(i)  # Append the current index

            return ans

        # Process each row in the matrix
        for row in matrix:
            # Update the histogram based on the current row
            for i, num in enumerate(row):
                hist[i] = 0 if num == '0' else hist[i] + 1  # Reset or increment histogram heights
            
            # Compute the maximum rectangle area for the current histogram
            ans = max(ans, largestRectangleArea(hist))

        return ans

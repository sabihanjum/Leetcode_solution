"""You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity."""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Initializing pointers for the top and bottom rows of the matrix
        top = 0
        bot = len(matrix) - 1

        # Binary search to find the potential row where the target might exist
        while top <= bot:
            mid = (top + bot) // 2  # Middle row index
            
            # Check if the target lies within the range of this row
            if matrix[mid][0] < target and matrix[mid][-1] > target:
                break  # The target must be in this row
                
            # If the target is less than the first element of the middle row,
            # search in the upper half (move the bottom pointer up)
            elif matrix[mid][0] > target:
                bot = mid - 1
                
            # If the target is greater than the last element of the middle row,
            # search in the lower half (move the top pointer down)
            else:
                top = mid + 1

        # We assume the target is in the row (top + bot) // 2
        row = (top + bot) // 2

        # Binary search within the row to find the exact target
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2  # Middle element index within the row

            # If the target is found, return True
            if matrix[row][mid] == target:
                return True

            # If the middle element is greater than the target, search left half
            elif matrix[row][mid] > target:
                right = mid - 1

            # If the middle element is less than the target, search right half
            else:
                left = mid + 1

        # If we finish the loop and haven't found the target, return False
        return False

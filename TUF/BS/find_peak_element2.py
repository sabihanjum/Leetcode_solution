"""A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time."""

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # Initialize the search bounds, l is the left bound, r is the right bound
        l, r = 0, len(mat) - 1
        
        # Perform binary search on the rows of the matrix
        while l < r:
            # Find the middle row
            mid = (l + r) >> 1  # Equivalent to (l + r) // 2, but more optimized bit shift
            
            # Find the column index of the maximum element in the middle row
            j = mat[mid].index(max(mat[mid]))
            
            # Check if the element at (mid, j) is a peak compared to the element in the row below
            if mat[mid][j] > mat[mid + 1][j]:
                # If it's greater than the corresponding element in the next row, we search in the upper half
                r = mid
            else:
                # Otherwise, search in the lower half
                l = mid + 1
        
        # When l == r, we have found the peak row, return the row index and the index of the maximum element in that row
        return [l, mat[l].index(max(mat[l]))]

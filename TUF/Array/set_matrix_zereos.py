class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Initialize flags to check if the first row and first column need to be zeroed
        row_flag = col_flag = False
        rows = len(matrix)
        cols = len(matrix[0])

        # First pass: Identify the rows and columns that need to be zeroed
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:  # Found a zero element
                    # Check if it's in the first row
                    if row == 0:
                        row_flag = True
                    # Check if it's in the first column
                    if col == 0:
                        col_flag = True

                    # Mark the first cell of the row and column for zeroing later
                    elif row != 0 and col != 0:
                        matrix[row][0] = 0  # Mark the first cell of the row
                        matrix[0][col] = 0  # Mark the first cell of the column
        
        # Second pass: Use the markers in the first row and column to set the appropriate cells to zero
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0  # Zero out the cell if its row or column is marked

        # If the first row needs to be zeroed, set all its cells to zero
        if row_flag:
            matrix[0] = [0] * cols

        # If the first column needs to be zeroed, set all its cells to zero
        if col_flag:
            for row in range(rows):
                matrix[row][0] = 0

# The function modifies the matrix in-place without returning anything.

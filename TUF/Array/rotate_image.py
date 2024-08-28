class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Step 1: Transpose the matrix (convert rows to columns)
        # We iterate through the matrix, and for each element matrix[i][j],
        # we swap it with matrix[j][i] where j < i to avoid re-swapping
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row to complete the 90-degree rotation
        # We iterate through each row and swap the elements in the row
        # from the beginning and the end until we reach the middle
        for j in range(len(matrix) // 2):
            for i in range(len(matrix)):
                matrix[i][j], matrix[i][len(matrix) - 1 - j] = matrix[i][len(matrix) - 1 - j], matrix[i][j]

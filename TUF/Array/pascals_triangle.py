class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]  # Initialize the result with the first row of Pascal's Triangle

        for i in range(numRows - 1):  # Loop to generate each row, starting from the second row
            temp = [0] + res[-1] + [0]  # Add padding of zeros to the previous row to calculate the new row
            row = []  # Initialize the new row
            for j in range(len(res[-1]) + 1):  # Loop through the elements to generate the current row
                row.append(temp[j] + temp[j+1])  # Each element is the sum of the two elements above it
            res.append(row)  # Add the newly generated row to the result list

        return res  # Return the final result containing all rows of Pascal's Triangle

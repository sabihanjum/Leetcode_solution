"""Given an array of N integers and Q queries of indices. Return a list NGEs[] where NGEs[i] stores the count of elements strictly greater than the current element (arr[indices[i]]) to the right of indices[i]."""

class Solution:
    def count_NGEs(self, N, arr, queries, indices):
        """
        Count the number of next greater elements (NGEs) for each given index.

        Args:
        N: int - Total number of elements in the array.
        arr: list[int] - The array of integers.
        queries: int - Number of queries (not directly used in this implementation).
        indices: list[int] - The list of indices for which NGEs need to be counted.

        Returns:
        list[int] - A list containing the count of NGEs for each index in 'indices'.
        """
        # Initialize the result list to store counts of NGEs for each index
        result = []

        # Loop through each index in the 'indices' list
        for i in indices:
            count = 0  # Initialize count of NGEs for the current index
            
            # Iterate over the elements to the right of index `i`
            for j in range(i + 1, N):
                if arr[i] < arr[j]:  # Check if the current element is greater than arr[i]
                    count += 1  # Increment the count if it's a Next Greater Element
            
            # Append the count of NGEs for this index to the result list
            result.append(count)

        # Return the list of counts
        return result

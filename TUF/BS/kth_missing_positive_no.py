"""Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array."""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Binary search initialization
        l, r = 0, len(arr) - 1  # 'l' is the left boundary, 'r' is the right boundary

        # Perform binary search to find the position where the k-th missing positive should be
        while l <= r:
            m = (l + r) // 2  # Calculate the middle index
            # Calculate how many numbers are missing up to the position 'm'
            # This is done by comparing the value at 'arr[m]' with the expected value 'm+1'
            missing = arr[m] - (m + 1)
            
            # If the missing count is less than 'k', move the left boundary to narrow down the search
            if missing < k:
                l = m + 1  # Narrow search to the right half (increase left boundary)
            else:
                r = m - 1  # Narrow search to the left half (decrease right boundary)

        # Once the loop ends, 'r' will be the last position where the missing numbers count is less than 'k'
        # The k-th missing positive number will be at position 'r + k + 1'
        return r + k + 1

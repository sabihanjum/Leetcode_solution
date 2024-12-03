"""You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window."""
from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the maximum values in every sliding window of size `k` in the list `nums`.

        Args:
        nums (List[int]): The list of integers.
        k (int): The size of the sliding window.

        Returns:
        List[int]: A list of the maximum values for each sliding window.
        """
        output = []  # To store the result
        q = collections.deque()  # Deque to maintain indices of elements in the current window
        l = 0  # Left boundary of the sliding window
        r = 0  # Right boundary of the sliding window

        # Iterate through the array
        while r < len(nums):
            # Remove indices of smaller elements from the back of the deque
            # as they can't be the maximum for the current or future windows
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # Add the current index to the deque
            q.append(r)

            # Remove indices of elements that are no longer in the current window
            if q[0] < l:
                q.popleft()

            # When the window size reaches `k`
            if (r + 1) >= k:
                # The element at the front of the deque is the largest in the current window
                output.append(nums[q[0]])
                # Move the left pointer to shrink the window
                l += 1

            # Expand the window by moving the right pointer
            r += 1

        return output

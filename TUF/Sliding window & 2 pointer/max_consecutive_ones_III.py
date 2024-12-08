"""Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's."""

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        ans = 0  # Variable to store the maximum length of subarray with at most `k` zeros
        l = 0  # Left pointer of the sliding window

        # Iterate over the array using the right pointer `r`
        for r, num in enumerate(nums):
            if num == 0:
                # Decrement `k` when encountering a zero, as we are "using up" one of our flips
                k -= 1
            # When `k` becomes negative, it means we have exceeded the allowable number of flips
            while k < 0:
                if nums[l] == 0:
                    # If the left element is a zero, move the left pointer to the right
                    # and "free up" a flip
                    k += 1
                l += 1  # Shrink the window from the left
            # Update the maximum length of the subarray
            ans = max(ans, r - l + 1)

        return ans

"""You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array."""

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        Calculate the sum of the range (max - min) for all subarrays in the array.

        Args:
        nums: List[int] - The input list of integers.

        Returns:
        int - The sum of all subarray ranges.
        """
        stack = []
        nums.append(float('inf'))  # Append sentinel value to handle all elements in the stack
        res = 0  # Initialize the result
        
        # Calculate the contribution of each element as the maximum in subarrays
        for i in range(len(nums)):
            # While the current number is greater than the top of the stack
            while stack and nums[stack[-1]] < nums[i]:
                j = stack.pop()  # Index of the current maximum element
                r = i - 1  # Right boundary where nums[j] is the maximum
                l = stack[-1] + 1 if stack else 0  # Left boundary where nums[j] is the maximum
                # Add the contribution of nums[j] as a maximum
                res += nums[j] * (r - j + 1) * (j - l + 1)
            stack.append(i)
        
        stack.clear()  # Clear the stack for reuse
        nums.pop()  # Remove the sentinel value
        nums.append(float('-inf'))  # Append sentinel value for the minimum calculation

        # Calculate the contribution of each element as the minimum in subarrays
        for i in range(len(nums)):
            # While the current number is less than the top of the stack
            while stack and nums[stack[-1]] > nums[i]:
                j = stack.pop()  # Index of the current minimum element
                r = i - 1  # Right boundary where nums[j] is the minimum
                l = stack[-1] + 1 if stack else 0  # Left boundary where nums[j] is the minimum
                # Subtract the contribution of nums[j] as a minimum
                res -= nums[j] * (r - j + 1) * (j - l + 1)
            stack.append(i)

        return res

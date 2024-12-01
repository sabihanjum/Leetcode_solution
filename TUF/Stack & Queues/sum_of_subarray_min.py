"""Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7."""
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        Calculate the sum of the minimum values of all subarrays in the array.

        Args:
        arr: List[int] - The input array.

        Returns:
        int - The sum of the minimum values of all subarrays modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7  # Modulo to avoid overflow
        res = 0  # Initialize the result
        stack = []  # Monotonic stack to keep track of indices and values (index, value)

        # Iterate over the array
        for i, n in enumerate(arr):
            # While the current element is smaller than the top of the stack
            while stack and n < stack[-1][1]:
                j, m = stack.pop()  # Pop the top element (index, value)

                # Calculate the number of subarrays where `m` is the minimum
                left = j - stack[-1][0] if stack else j + 1  # Distance to the previous smaller element
                right = i - j  # Distance to the next smaller element

                # Add the contribution of `m` to the result
                res = (res + m * left * right) % MOD

            # Push the current index and value onto the stack
            stack.append((i, n))

        # Handle any remaining elements in the stack
        for i in range(len(stack)):
            j, n = stack[i]  # Get the index and value of the element
            left = j - stack[i - 1][0] if i > 0 else j + 1  # Distance to the previous smaller element
            right = len(arr) - j  # Distance to the end of the array

            # Add the contribution of the remaining elements to the result
            res = (res + n * left * right) % MOD

        return res

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            # If the input list is empty, the maximum product is 0.
            return 0

        # Initialize the maximum product (max_pro) and minimum product (min_pro)
        # with the first element of the array. This helps handle cases where the
        # array has only one element.
        max_pro, min_pro = nums[0], nums[0]

        # Initialize the result with the first element.
        result = max_pro

        # Iterate through the array starting from the second element.
        for i in range(1, len(nums)):
            curr = nums[i]

            # Calculate temporary maximum product considering the current element.
            # We need to consider the current element itself, the product of the
            # current element with the previous maximum product, and the product of
            # the current element with the previous minimum product.
            temp_max = max(curr, max_pro * curr, min_pro * curr)
            
            # Update the minimum product in a similar way to handle negative numbers.
            min_pro = min(curr, max_pro * curr, min_pro * curr)

            # Update the maximum product to the temporary maximum calculated.
            max_pro = temp_max

            # Update the result with the maximum value found so far.
            result = max(max_pro, result)
        
        return result

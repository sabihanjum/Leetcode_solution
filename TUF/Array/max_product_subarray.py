class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize prod1 and prod2 to the first element of the array.
        # prod1 will track the maximum product up to the current element.
        # prod2 will track the minimum product up to the current element (to handle negative numbers).
        prod1 = nums[0]
        prod2 = nums[0]
        
        # Initialize result to the first element, as the maximum product cannot be less than the first element.
        result = nums[0]

        # Loop through the array starting from the second element (index 1).
        for i in range(1, len(nums)):
            # Store the current maximum product temporarily.
            # It's important to use `prod1 * nums[i]` and `prod2 * nums[i]` to capture both maximum and minimum product
            # so far because multiplying two negative numbers could give a higher positive product.
            temp = max(nums[i], prod1 * nums[i], prod2 * nums[i])
            
            # Update prod2 to the minimum of current element, prod1 * nums[i], or prod2 * nums[i].
            # This is crucial as multiplying by a negative number can turn a large number into a small one,
            # so we track the minimum product for future iterations.
            prod2 = min(nums[i], prod1 * nums[i], prod2 * nums[i])
            
            # Update prod1 to the maximum product found so far (this is what we stored in temp).
            prod1 = temp

            # Update the result to be the maximum product found so far.
            result = max(result, prod1)
        
        # Return the overall maximum product.
        return result

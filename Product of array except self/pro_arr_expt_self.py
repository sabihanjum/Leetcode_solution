class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)  # Get the length of the input list
        
        # Initialize prefix and suffix product lists with 1
        prefix = [1] * n  # This will store the product of all elements to the left of each element
        suffix = [1] * n  # This will store the product of all elements to the right of each element

        # Compute prefix products
        for i in range(1, n):  # Start from the second element
            prefix[i] = prefix[i - 1] * nums[i - 1]  # Multiply the current prefix value by the previous element in nums

        # Compute suffix products
        for i in reversed(range(n - 1)):  # Start from the second-to-last element and go backwards
            suffix[i] = suffix[i + 1] * nums[i + 1]  # Multiply the current suffix value by the next element in nums

        # Compute the result by multiplying prefix and suffix products for each element
        return [prefix[i] * suffix[i] for i in range(n)]  # The result for each element is the product of its prefix and suffix

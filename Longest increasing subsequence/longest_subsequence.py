class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize an array LIS where each element represents the length of the longest increasing subsequence ending at that index
        LIS = [1] * len(nums)

        # Iterate over the list in reverse order starting from the second last element to the first
        for i in range(len(nums) - 1, -1, -1):
            # For each element nums[i], check all elements to its right
            for j in range(i + 1, len(nums)):
                # If nums[i] is less than nums[j], it means nums[j] can extend the increasing subsequence ending at nums[i]
                if nums[i] < nums[j]:
                    # Update the LIS value at index i to the maximum of its current value or 1 plus the LIS value at index j
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        # Return the maximum value in the LIS array, which represents the length of the longest increasing subsequence in the array
        return max(LIS)

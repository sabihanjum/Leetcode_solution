class Solution:
    def threeSum(self, nums):
        nums.sort()  # Sort the array to use two-pointer technique
        res = []  # List to store the resulting triplets

        # Iterate through the array
        for i in range(len(nums)):
            # Skip the same elements to avoid duplicates in the result
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1  # Initialize two pointers

            # Use two-pointer technique to find the other two elements
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1  # Increase the left pointer to get a larger sum
                else:
                    right -= 1  # Decrease the right pointer to get a smaller sum
        
        return res  # Return the list of triplets

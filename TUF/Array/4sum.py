class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array to make it easier to use the two-pointer technique
        res = []  # This will store the final list of quadruplets

        n = len(nums)  # Get the length of the array

        # Iterate through the array with the first pointer `i`
        for i in range(n):
            # Skip duplicate elements for the first pointer to avoid duplicate quadruplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Iterate through the array with the second pointer `j`
            for j in range(i + 1, n):
                # Skip duplicate elements for the second pointer
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Initialize two pointers `k` and `l`
                k = j + 1
                l = n - 1

                # Use the two-pointer technique to find the remaining two elements
                while k < l:
                    _sum = nums[i] + nums[j] + nums[k] + nums[l]  # Calculate the sum of the four elements

                    # Check if the sum matches the target
                    if _sum == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]  # Create a quadruplet
                        res.append(temp)  # Add the quadruplet to the result list
                        k += 1  # Move the left pointer to the right
                        l -= 1  # Move the right pointer to the left

                        # Skip duplicate elements for the third pointer
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        # Skip duplicate elements for the fourth pointer
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

                    # If the sum is less than the target, move the left pointer to the right to increase the sum
                    elif _sum < target:
                        k += 1
                    # If the sum is greater than the target, move the right pointer to the left to decrease the sum
                    else:
                        l -= 1

        return res  # Return the list of unique quadruplets

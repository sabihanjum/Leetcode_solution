class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left pointer to the beginning of the list
        # Initialize right pointer to the end of the list
        l, r = 0, len(nums) - 1
        
        # Loop until left pointer is less than or equal to right pointer
        while l <= r:
            # Calculate the middle index
            mid = (l+r) // 2
            
            # If target is found at the middle index, return the index
            if target == nums[mid]:
                return mid

            # If left portion is sorted
            if nums[l] <= nums[mid]:
                # Check if target lies within the left sorted portion
                if target > nums[mid] or target < nums[l]:
                    # If not, move the left pointer to mid + 1
                    l = mid + 1
                else:
                    # If yes, move the right pointer to mid - 1
                    r = mid - 1

            # If right portion is sorted
            else:
                # Check if target lies within the right sorted portion
                if target < nums[mid] or target > nums[r]:
                    # If not, move the right pointer to mid - 1
                    r = mid - 1
                else:
                    # If yes, move the left pointer to mid + 1
                    l = mid + 1
        
        # If target is not found, return -1
        return -1

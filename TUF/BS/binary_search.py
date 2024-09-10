class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Step 1: Determine the length of the list
        n = len(nums)
        
        # Step 2: Initialize the 'low' and 'high' pointers for binary search
        low = 0  # Start of the list
        high = n - 1  # End of the list

        # Step 3: Perform the binary search
        while low <= high:
            # Find the middle index between 'low' and 'high'
            mid = (low + high) // 2
            
            # If the target is found at the mid position, return the index
            if nums[mid] == target:
                return mid
            
            # If the target is greater than the middle element,
            # discard the left half and search in the right half
            elif target > nums[mid]:
                low = mid + 1
            
            # If the target is smaller than the middle element,
            # discard the right half and search in the left half
            else:
                high = mid - 1
        
        # Step 4: If the target is not found, return -1
        return -1

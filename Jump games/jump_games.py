from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> int:
        # If the list has 1 or fewer elements, no jump is needed
        if len(nums) <= 1:
            return 0
        
        # Initialize the number of jumps to 0
        jumps = 0
        # Initialize the current end of the range that can be reached with the current number of jumps
        current_end = 0
        # Initialize the farthest point that can be reached
        farthest = 0
        
        # Iterate through the array except the last element
        for i in range(len(nums) - 1):
            # Update the farthest point that can be reached
            farthest = max(farthest, i + nums[i])
            
            # If the current index reaches the end of the current range
            if i == current_end:
                # Increment the number of jumps
                jumps += 1
                # Update the end of the current range to the farthest point reached
                current_end = farthest
                
                # If the current end reaches or exceeds the last index, we can stop
                if current_end >= len(nums) - 1:
                    break
        
        # Return the total number of jumps needed
        return jumps

"""You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1]."""

class Solution:
    def jump(self, nums: list[int]) -> int:
        # Initialize the number of jumps needed
        ans = 0
        
        # The 'end' variable marks the range of the current jump
        end = 0
        
        # 'farthest' keeps track of the farthest point that can be reached
        farthest = 0

        # Iterate over the array, excluding the last element
        # because we do not need to jump from the last index
        for i in range(len(nums) - 1):
            # Update the farthest point reachable from the current position
            farthest = max(farthest, i + nums[i])
            
            # If the farthest point reaches or exceeds the last index, we can stop
            if farthest >= len(nums) - 1:
                ans += 1  # Count the final jump to reach the end
                break

            # If we reach the end of the current jump range
            if i == end:
                ans += 1        # Increment the number of jumps
                end = farthest  # Update the range for the next jump level

        return ans

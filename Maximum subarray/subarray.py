class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]   #assume the first number is the maximum number
        curr = nums[0]         #start with the first number in array
        for i in range(1, len(nums)):           #iterate through each element of the array
            curr = max(nums[i], curr+nums[i])   #take the larger one between current number and adding it to previous number
            max_so_far = max(max_so_far, curr)  #if current number is gretaer than max so far update max so far
        return max_so_far                       #return the largest number found
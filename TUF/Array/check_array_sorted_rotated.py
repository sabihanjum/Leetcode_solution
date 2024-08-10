class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0  #voilation

        for i in range(len(nums)):
            if nums[i] > nums[(i+1) % len(nums)]:
                count += 1

        return count <= 1
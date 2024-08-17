class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xorr = 0
        for num in nums:
            xorr^=num
        return xorr
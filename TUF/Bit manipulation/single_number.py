"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space."""

class Solution(object):
    def singleNumber(self, nums):
        map = {}
        if ( nums == [] ):
            return -1
        for d in nums:
            if ( d in map):
                del map[d]
            else:
                map[d] = 1
        return list(map.keys())[0]
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2    #merge two arrays into an array
        nums.sort()             #sort the merged array
        l1 = len(nums)
        if l1 % 2 != 0:            #odd number of element in total
            return nums[l1 // 2]   #return middle one
        else:
            mid = l1 // 2           #return average of two middle
            return (nums[mid - 1] + nums[mid]) / 2     #divide by 2 to get median

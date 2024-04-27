class Solution: 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                                          #O(nlogn)
        ans = []                                            
        n = len(nums)                                        #number of element in the list
        i = 0                                                #point to first number
        while i < n:                          #try all possible triplets with first point "i"
            if nums[i] > 0: break   
            l = i + 1                         #pointer for second number
            r = n - 1                         #pointer for third number
            while l < r:   
                sum3 = nums[i] + nums[l] + nums[r]          #Calculate the sum of current triplet
                if sum3 == 0:         #if equal to zero then add it into answer and move pointer ahead
                    ans.append([nums[i], nums[l], nums[r]])  #add this triplet into answer
                    while l+1 < n and nums[l+1] == nums[l]: l += 1  #skip same number
                    l += 1                #move pointer "l" forward
                    r -= 1                #move pointer "r" backward
                elif sum3 < 0: l += 1     #if not equal to zero and not greater than zero
                else: r -= 1              #if not less than zero than it is greater than zero
            while i+1 < n and nums[i+1] == nums[i]: i += 1     #skip same number
            i += 1                        #move pointer "i" forward
        return ans                        #return final answer

 


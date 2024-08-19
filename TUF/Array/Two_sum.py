class Solution(object):  
    def twoSum(self, nums, target): 
        d={}                            #Create a dictionary to store the number and it's index
        for i, num in enumerate(nums):  #Iterate through the list of number with their indices
            t = target -num             #Find the complementary number
            if t in d:                  #If the complementary number is already in the list
                return[d[t], i]         #Returbn the indices of both number
            d[num] = i                  # Add the number and it's index
        return[]                        #if no such pair exist, return an empty array
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0  # This variable will store the total number of subarrays that sum up to 'k'
        curSum = 0  # This will store the cumulative sum of elements as we iterate through the array
        prefixSum = {0: 1}  # Dictionary to store the frequency of cumulative sums (prefix sums)
                            # We initialize with 0:1 to handle the case where a subarray itself equals 'k'
        
        # Iterate through each number in the input list 'nums'
        for n in nums:
            curSum += n  # Update the current cumulative sum by adding the current number
            
            diff = curSum - k  # Calculate the difference needed to reach the sum 'k'
            
            # If 'diff' exists in 'prefixSum', it means there's a subarray that sums to 'k'
            # Add the count of such subarrays to 'res'
            res += prefixSum.get(diff, 0)
            
            # Update the 'prefixSum' dictionary with the current cumulative sum
            # If 'curSum' is already in 'prefixSum', increment its count, otherwise, set it to 1
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        
        return res  # Return the total count of subarrays that sum up to 'k'

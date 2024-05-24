class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    ans = 0  # Initialize the answer to 0, which will store the number of subarrays that sum to k
    prefix = 0  # Initialize prefix sum to 0
    count = collections.Counter({0: 1})  # Initialize a counter to store the frequency of prefix sums, starting with 0 sum having a frequency of 1

    for num in nums:  # Iterate through each number in the input list
      prefix += num  # Update the prefix sum by adding the current number
      ans += count[prefix - k]  # If (prefix - k) exists in the counter, add its frequency to ans
      count[prefix] += 1  # Increment the frequency of the current prefix sum in the counter

    return ans  # Return the total number of subarrays that sum to k

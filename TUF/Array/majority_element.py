class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize an empty dictionary to store the counts of each element
        sums = {}

        # Iterate through each number in the input list 'nums'
        for n in nums:
            # If the number 'n' is not in the dictionary, add it with a count of 1
            if n not in sums:
                sums[n] = 1
            else:
                # If the number 'n' is already in the dictionary, increment its count by 1
                sums[n] += 1
            
            # Check if the current number's count exceeds half the length of 'nums'
            if sums[n] > len(nums) / 2:
                # If it does, return 'n' as it is the majority element
                return n
            
            # Time Complexity (TC) of the above approach is O(n), where n is the length of 'nums'

        # If the above loop does not return a result (which shouldn't happen in a valid input),
        # this line can be used as an alternative approach:
        # Sort the list and return the middle element, which will be the majority element
        # return sorted(nums)[len(nums)//2]
        # Time Complexity (TC) of this approach is O(n log n) due to sorting

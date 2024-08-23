class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Create a list of all positive numbers from the input array
        positives = [num for num in nums if num > 0]
        
        # Create a list of all negative numbers from the input array
        negatives = [num for num in nums if num < 0]
        
        # Initialize an empty list to store the rearranged result
        result = []

        # Iterate through half the length of the input array (assuming equal number of positives and negatives)
        for i in range(len(nums) // 2):
            # Append a positive number followed by a negative number in each iteration
            result.append(positives[i])
            result.append(negatives[i])
        
        # Return the rearranged list
        return result

class Solution:
    def maxLen(self, n, arr):
        # First, we calculate the prefix sum for the array
        # Each element in the array will be updated to be the sum of itself and all previous elements
        for i in range(1, n):
            arr[i] += arr[i-1]
        
        # Initialize the result variable to store the maximum length of subarray with sum 0
        res = 0
        
        # Create a dictionary to store the first occurrence of each prefix sum
        dc = dict()
        
        # Iterate through the array with the prefix sums
        for i, sm in enumerate(arr):
            # If the prefix sum is 0, it means the subarray from the start to this index has a sum of 0
            if sm == 0:
                res = max(res, i+1)  # Update the result with the maximum length found
                
            # If the prefix sum has been seen before, it means the subarray between the previous occurrence
            # and the current index has a sum of 0
            elif sm in dc:
                res = max(res, i - dc[sm])  # Update the result with the maximum length found
                
            else:
                # If this prefix sum has not been seen before, store the index in the dictionary
                dc[sm] = i
                
        # Return the maximum length of the subarray with sum 0
        return res

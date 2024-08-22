"""You are given an array arr[] containing positive integers. 
These integers can be from 1 to p, and some numbers may be repeated or absent. 
Your task is to count the frequency of all numbers that lie in the range 1 to n."""

class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # Initialize an empty dictionary to store the frequency of each element in the array
        hash_map = {}

        # Iterate through each element in the array 'arr'
        for num in arr:
            # If the element 'num' is already in the hash_map, increment its frequency count by 1
            if num in hash_map:
                hash_map[num] += 1
            else:
                # If the element 'num' is not in the hash_map, add it with an initial count of 1
                hash_map[num] = 1
                
        # Iterate through numbers from 1 to N (inclusive)
        for i in range(1, N+1):
            # If the number 'i' is in the hash_map, update the corresponding index in the array 'arr'
            # with the frequency count from the hash_map
            if i in hash_map:
                arr[i-1] = hash_map[i]
            else:
                # If the number 'i' is not in the hash_map, set the corresponding index in 'arr' to 0
                arr[i-1] = 0

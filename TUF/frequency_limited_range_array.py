class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        
        hash_map = {}
        for num in arr:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
                
        for i in range(1, N+1):
            if i in hash_map:
                arr[i-1] = hash_map[i]
            else:
                arr[i-1] = 0
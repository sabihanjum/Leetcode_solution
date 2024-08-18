class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        map = {}
        len = 0
        sum = 0
        
        for i in range(n):
            sum += arr[i]
            if sum == k:
                len = max(len, i+1)
                
            if sum - k in map:
                len = max(len, i-map[sum-k])
                
            if sum not in map:
                map[sum] = i
        return len
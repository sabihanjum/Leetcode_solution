class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0    #edge case of empty array
        
        water, n = 0, len(height)  #initialize the counter and length of array
        max_left, max_right = [None] * n, [None] * n  #create dynamic array to store maximum bar on left/right side
        max_left[0], max_right[-1] = height[0], height[-1]  #initialize the maximum bar left and rightfrom first and last element respectively
        
        for i in range(1, n):    #start from the index 1 to avoid duplicate counting at the edge
            max_left[i] = max(max_left[i-1], height[i])  #update the left side maximum barrier 
            
        for i in range(n-2, 0, -1):   #similarly update right side maximum barrier
            max_right[i] = max(max_right[i+1], height[i])
            water += min(max_left[i], max_right[i]) - height[i] #add up the area that can trapped
            
        return water        #return total amount of water can trapped
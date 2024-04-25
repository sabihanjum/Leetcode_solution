class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        water, n = 0, len(height)
        max_left, max_right = [None] * n, [None] * n
        max_left[0], max_right[-1] = height[0], height[-1]
        
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])
            
        for i in range(n-2, 0, -1):
            max_right[i] = max(max_right[i+1], height[i])
            water += min(max_left[i], max_right[i]) - height[i]
            
        return water
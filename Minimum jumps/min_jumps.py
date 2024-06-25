class Solution:
    def minJumps(self, arr, n):
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1
        
        # maxReach stores the maximum reachable index in the array.
        maxReach = arr[0]
        # step stores the number of steps we can still take.
        step = arr[0]
        # jump stores the number of jumps necessary to reach that maxReach position.
        jump = 1
        
        for i in range(1, n):
            # Check if we have reached the end of the array.
            if i == n-1:
                return jump
            
            # Updating maxReach.
            maxReach = max(maxReach, i + arr[i])
            
            # Decrease the step by 1.
            step -= 1
            
            # If no further steps left.
            if step == 0:
                # We must have used a jump.
                jump += 1
                
                # Check if the current index/position or lesser index is the maximum reach point from the previous indexes.
                if i >= maxReach:
                    return -1
                
                # Re-initialize the steps to the amount of steps to reach maxReach from position i.
                step = maxReach - i
        
        return -1

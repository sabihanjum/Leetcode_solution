"""You are given 2 numbers (n , m); the task is to find n√m (nth root of m)."""

class Solution:
    def func(self, mid, n, m):
        ans = 1
        for i in range(1, n+1):
            ans *= mid
            if ans > m:
                return 2  # If the result exceeds m, return 2
        if ans == m:
            return 1  # If ans is equal to m, return 1
        return 0  # If ans is less than m, return 0
    
    def NthRoot(self, n, m):
        # Binary search to find the nth root of m
        low = 1
        high = m
        while low <= high:
            mid = (low + high) // 2
            midN = self.func(mid, n, m)  # Call the func method with self
            if midN == 1:
                return mid  # If the result is exactly m, return mid
            elif midN == 0:
                low = mid + 1  # Continue searching in the right half
            else:
                high = mid - 1  # Continue searching in the left half
        return -1  # Return -1 if no nth root exists

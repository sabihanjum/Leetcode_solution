class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize a list with base cases:
        # ways[0] = 1 (1 way to stay at the ground step without climbing)
        # ways[1] = 1 (1 way to reach the first step)
        # ways[2] = 2 (2 ways to reach the second step: [1+1] or [2])
        ways = [1, 1, 2]
        
        # Calculate number of ways for each step from 3 to n
        for step in range(3, n + 1):
            # The number of ways to reach step i is the sum of ways to reach step i-1 and step i-2
            # This is because you can reach step i either from step i-1 (taking 1 step) or from step i-2 (taking 2 steps)
            ways.append(ways[step-1] + ways[step-2])
        
        # Return the number of ways to reach the n-th step
        return ways[n]

"""Given an array arr of size n of non-negative integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.

Note: Answer can be very large, so, output answer modulo 109+7."""

class Solution:
    def perfectSum(self, arr, n, sum):
        # Initialize a 2D dp array with -1, which will store intermediate results
        # dp[i][j] will represent the number of ways to achieve the sum 'j' using the first 'i' elements
        dp = [[-1] * (sum + 1) for _ in range(n + 1)]
        
        # Define a large modulus to prevent overflow of large numbers in the result
        mod = int(1e9+7)
        
        # Recursive function to find the number of subsets that sum up to the given target sum
        def solve(arr, i, n, sum):
            # Base case: if we've reached the end of the array
            if i >= n:
                # Return 1 if sum is exactly 0 (an empty subset can achieve this), otherwise return 0
                return sum == 0

            # If we have already calculated the value for dp[i][sum], use it to save computation
            if dp[i][sum] != -1:
                return dp[i][sum]
            
            # Initialize a variable to track the count of subsets including the current element
            a = 0
            # Check if the current element can be included without exceeding the remaining sum
            if sum - arr[i] >= 0:
                # Recursive call by including arr[i] in the subset
                a = solve(arr, i + 1, n, sum - arr[i]) % mod
            
            # Recursive call by excluding arr[i] from the subset
            b = solve(arr, i + 1, n, sum) % mod
            
            # Store the result of including or excluding the current element in dp
            dp[i][sum] = (a + b) % mod
            
            return dp[i][sum]

        # Call the recursive function starting with the first element and the target sum
        return solve(arr, 0, n, sum)

# Example usage:
# solution = Solution()
# print(solution.perfectSum([1, 2, 3], 3, 4))  
# Expected output: number of subsets of [1, 2, 3] that sum up to 4

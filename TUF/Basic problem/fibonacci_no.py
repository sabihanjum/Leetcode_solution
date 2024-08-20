class Solution:
    def fib(self, n: int) -> int:
        # Base case: if n is 0, the Fibonacci number is 0
        if n == 0:
            return 0

        # Base case: if n is 1, the Fibonacci number is 1
        if n == 1:
            return 1
        
        # Initialize the first two Fibonacci numbers
        prev1, prev2 = 0, 1
        
        # Variable to hold the current Fibonacci number
        temp = 0
        
        # Loop to calculate Fibonacci numbers from 2 to n
        for i in range(2, n + 2):
            # The current Fibonacci number is the sum of the previous two
            temp = prev1 + prev2
            
            # Update the previous two Fibonacci numbers for the next iteration
            prev2 = prev1
            prev1 = temp
        
        # Return the nth Fibonacci number
        return temp

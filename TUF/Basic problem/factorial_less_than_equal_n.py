class solution:
    def factorialNumbers(self, n):
        # Initialize an empty list to store factorial numbers
        arr = []
        
        # Helper function to calculate and store factorial numbers recursively
        def helper(fac_of, nxt):
            # If the current factorial value is less than or equal to n, store it in the list
            if fac_of <= n:
                arr.append(fac_of)
                # Recursively call the helper function with the next factorial value and incremented nxt
                helper(fac_of * (nxt + 1), nxt + 1)
        
        # Start the recursion with the first factorial (1!) and start the next value as 1
        helper(1, 1)
        
        # Return the list of factorial numbers
        return arr

class solution:
    def evenlyDivides(self, N):
        # Initialize a counter to keep track of digits that evenly divide N
        count = 0
        
        # Store the original value of N to use it in modulus operations
        original = N
        
        # Loop through each digit in the number
        while N > 0:
            # Get the last digit of N
            d = N % 10
            
            # Check if the digit is not zero and divides the original number evenly
            if d != 0 and original % d == 0:
                # If the condition is met, increment the count by 10
                count += 10
            
            # Remove the last digit from N (integer division by 10)
            N //= 10
        
        # Return the final count
        return count


def is_armstrong(num):
    # Calculate the number of digits in the given number
    k = len(str(num))
    
    # Initialize the sum of digits raised to the power of k to 0
    sum = 0
    
    # Copy the value of the input number to a temporary variable n
    n = num
    
    # Iterate through each digit of the number
    while n > 0:
        # Extract the last digit of the number
        ld = n % 10
        
        # Add the digit raised to the power of k to the sum
        sum += ld ** k
        
        # Remove the last digit from the number
        n = n // 10
    
    # Check if the sum of digits raised to the power of k equals the original number
    return sum == num



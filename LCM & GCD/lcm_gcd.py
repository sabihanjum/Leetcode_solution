class Solution:
    def lcmAndGcd(self, A, B):
        # Helper function to calculate the Greatest Common Divisor (GCD) using the Euclidean algorithm
        def gcd(a, b):
            while b:
                a, b = b, a % b  # Replace a with b and b with a % b until b is zero
            return a  # When b is zero, a is the GCD
        
        # Calculate the GCD of A and B
        gcd_val = gcd(A, B)
        
        # Calculate the LCM of A and B using the relation LCM(A, B) * GCD(A, B) = A * B
        lcm_val = (A * B) // gcd_val
        
        # Return a list containing the LCM and GCD
        return [lcm_val, gcd_val]


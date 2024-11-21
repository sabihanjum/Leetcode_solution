"""Given a number N. Find its unique prime factors in increasing order."""

import math

class Solution:
    def AllPrimeFactors(self, N):
        # Initialize an empty set to store unique prime factors
        factors = set([])

        # Loop through numbers starting from 2 up to the square root of N
        for i in range(2, math.floor(math.sqrt(N)) + 1):
            # Keep dividing N by i as long as i is a divisor of N
            while (N % i == 0):
                # Add i to the set of prime factors
                factors.add(i)
                # Divide N by i to continue finding the prime factor
                N = N // i
        
        # If N is greater than 1, it means N itself is a prime factor
        if N > 1:
            factors.add(N)

        # Return the sorted list of unique prime factors
        return sorted(factors)

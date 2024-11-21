"""Given an integer n, return the number of prime numbers that are strictly less than n."""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Create a boolean list to keep track of prime numbers
        primes = [True] * n
        primes[0] = primes[1] = False  # 0 and 1 are not primes

        # Start the sieve process
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                # Mark multiples of i as non-prime
                for j in range(i * i, n, i):
                    primes[j] = False
        
        # Count the number of primes
        return sum(primes)

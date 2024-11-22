"""You are given a positive number N. Using the concept of Sieve, compute its prime factorisation."""

class Solution:
    def sieve(self):
        """
        Placeholder for a sieve function, not implemented in this code snippet.
        """
        pass

    def sieveN(self, N):
        """
        Implements the Sieve of Eratosthenes to calculate the smallest prime factor (spf) 
        for every number from 1 to N.
        
        Parameters:
        N (int): The maximum number for which to compute the smallest prime factors.

        Returns:
        list[int]: A list where spf[i] represents the smallest prime factor of i.
        """
        # Initialize the spf array where spf[i] is initially i (assuming all are prime)
        spf = list(range(N + 1))
        
        # Calculate the square root of N (optimization for sieve)
        sqrt = int(N ** 0.5) + 1
        
        # Sieve of Eratosthenes logic to find the smallest prime factors
        for i in range(2, sqrt):
            # If spf[i] is still i, it means i is a prime number
            if spf[i] == i:
                # Mark multiples of i, starting from i*i, with i as their smallest prime factor
                for j in range(i * i, N + 1, i):
                    if spf[j] == j:  # Only update if the number has not been marked yet
                        spf[j] = i
        
        return spf

    def findPrimeFactors(self, N):
        """
        Finds all prime factors of a given number N using the smallest prime factor (spf) array.
        
        Parameters:
        N (int): The number for which to compute the prime factors.

        Returns:
        list[int]: A list of prime factors of N (with repetitions for multiple factors).
        """
        # Edge case: If N is less than or equal to 1, it has no prime factors
        if N <= 1:
            return []
        
        # Generate the smallest prime factor array for numbers up to N
        spf = self.sieveN(N)
        
        # List to store the prime factors of N
        factors = []
        
        # Decompose N into its prime factors using the spf array
        while N != 1:
            # Append the smallest prime factor of N to the factors list
            factors.append(spf[N])
            # Divide N by its smallest prime factor to continue decomposition
            N //= spf[N]
        
        return factors

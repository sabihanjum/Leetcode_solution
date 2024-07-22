class Solution:
    def sumOfDivisors(self, N):
        divisor_sum = 0

        for i in range(1, N + 1):
            divisor_sum += (i * (N // i))
        
        return divisor_sum

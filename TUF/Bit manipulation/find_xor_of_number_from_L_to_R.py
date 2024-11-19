"""You are given two integers L and R, your task is to find the XOR of elements of the range [L, R]."""

class Solution:
    def findXOR(self, l, r):
        # Function to find XOR of all numbers in the range [l, r]

        # Case 1: Both l and r are even
        if l & 1 == 0 and r & 1 == 0:
            # XOR for even range can be simplified as:
            # XOR(r) ^ XOR(l-1), where XOR(n) is XOR from 0 to n
            # This works because the XOR for alternate numbers follows a predictable pattern
            return r ^ (((r - l) // 2) & 1)

        # Case 2: l is even and r is odd
        if l & 1 == 0 and r & 1 == 1:
            # The XOR of an even-to-odd range alternates based on the length of the range
            return (((r - l + 1) // 2) & 1)

        # Case 3: l is odd and r is even
        if l & 1 == 1 and r & 1 == 0:
            # XOR for an odd-to-even range can be split and calculated using l, r, and the intermediate length
            return l ^ r ^ (((r - l - 1) // 2) & 1)

        # Case 4: Both l and r are odd
        if l & 1 == 1 and r & 1 == 1:
            # XOR for odd ranges can be calculated similar to even ranges, excluding the first odd number
            return l ^ (((r - l) // 2) & 1)

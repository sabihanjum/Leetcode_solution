class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        prefix_xor = 0
        count = 0
        xor_count = {0: 1}  # Initialize with 0 XOR occurring once

        for num in A:
            prefix_xor^=num
            # Check if there is a prefix XOR that would result in subarray XOR B
            if(prefix_xor ^ B) in xor_count:
                count += xor_count[prefix_xor ^ B]
            # Update the count of the current prefix XOR
            if prefix_xor in xor_count:
                xor_count[prefix_xor] += 1
            else:
                xor_count[prefix_xor] = 1
        return count

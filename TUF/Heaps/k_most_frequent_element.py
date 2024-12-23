"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order."""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to store the frequency of each number
        count = {}

        # Create a frequency list where the index represents the frequency
        # Initialize an empty list for each possible frequency value
        freq = [[] for i in range(len(nums) + 1)]

        # Count the frequency of each number in the input list
        for n in nums:
            count[n] = 1 + count.get(n, 0)  # Increment the count of the number

        # Group numbers by their frequency in the `freq` list
        for n, c in count.items():
            freq[c].append(n)  # Append the number to the list at the index `c`

        # Result list to store the top K frequent elements
        res = []

        # Traverse the frequency list in reverse order (from high frequency to low)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:  # For each number with frequency `i`
                res.append(n)  # Add the number to the result
                if len(res) == k:  # Stop if we've collected the top K elements
                    return res

        
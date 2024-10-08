"""Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.
Example 1:
Input: s = "tree"
Output: "eert"""

from collections import Counter, defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        # Create a dictionary that maps each character in the string to its frequency
        count = Counter(s)  # char -> frequency count
        
        # Create a defaultdict that maps frequencies to the list of characters with that frequency
        buckets = defaultdict(list)   # frequency -> [characters]

        # Populate the buckets dictionary: add each character to the list corresponding to its frequency
        for char, cnt in count.items():
            buckets[cnt].append(char)

        # Initialize an empty list to build the result
        res = []

        # Traverse from the highest possible frequency (length of the string) down to 1
        for i in range(len(s), 0, -1):
            # If any characters have the current frequency 'i', append them to the result
            # Each character is repeated 'i' times in the result string
            for c in buckets[i]:
                res += c * i  # Append character 'c', repeated 'i' times

        # Join the list of characters into a string and return it
        return "".join(res)


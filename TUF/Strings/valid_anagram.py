"""Given two strings s and t, return true if t is an anagramof s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true"""

class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
        # Define the number of letters in the English alphabet
        numberOfLetters = 26
        
        # Convert both strings to lowercase to handle case insensitivity
        s1 = s1.lower()
        s2 = s2.lower()

        # If the lengths of the two strings are not the same, they cannot be anagrams
        if len(s1) != len(s2):
            return False
        
        # Initialize a list to keep count of each letter (assuming only lowercase English letters)
        count = [0 for i in range(numberOfLetters)]

        # Traverse the first string and increment the count for each letter
        for i in range(len(s1)):
            count[ord(s1[i]) - ord('a')] += 1

        # Traverse the second string and decrement the count for each letter
        for i in range(len(s2)):
            count[ord(s2[i]) - ord('a')] -= 1

        # After processing both strings, all counts should be zero if they are anagrams
        for i in range(numberOfLetters):
            if count[i] != 0:
                return False
        
        # If all the counts are zero, the strings are anagrams
        return True

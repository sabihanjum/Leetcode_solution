"""Given a pair of strings of equal lengths, Geek wants to find the better string. The better string is the 
string having more number of distinct subsequences.
If both the strings have equal count of distinct subsequence then return str1."""

class Solution:
    def count_dist(self, s):
        # Initialize dp array where dp[i] represents the count of distinct subsequences up to the ith character in s
        dp = [0] * (len(s) + 1)
        
        # Base case: an empty string has only one subsequence, the empty subsequence
        dp[0] = 1
        
        # Dictionary to store the last occurrence index of each character in s
        last_occurrence = {}
        
        # Loop through each character in the string s (1-based indexing for dp)
        for i in range(1, len(s) + 1):
            # Each subsequence up to i can either include or exclude the current character
            # Hence, we double the count of distinct subsequences from the previous step
            dp[i] = 2 * dp[i - 1]
            
            # If the current character has appeared before, subtract the count of subsequences up to its last occurrence
            if s[i - 1] in last_occurrence:
                dp[i] -= dp[last_occurrence[s[i - 1]] - 1]
            
            # Update the last occurrence of the current character to the current index
            last_occurrence[s[i - 1]] = i

        # The last element in dp contains the count of distinct subsequences for the entire string
        return dp[len(s)]

    def betterString(self, str1, str2):
        # Compare the distinct subsequences count of both strings using count_dist
        # Return the string with a higher count; if equal, return str1 by default
        if self.count_dist(str1) >= self.count_dist(str2):
            return str1
        else:
            return str2
        
        
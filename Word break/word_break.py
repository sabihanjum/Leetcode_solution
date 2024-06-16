from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert the wordDict list to a set for faster lookup
        d = set(wordDict)
        N = len(s)

        # Initialize a DP array with False values, of size N+1
        dp = [False for _ in range(N + 1)]
        # Set the base case: an empty string can always be segmented
        dp[0] = True

        # Iterate over each possible start position in the string
        for start in range(N):
            # If the current start position cannot form a valid segment, skip it
            if not dp[start]:
                continue
            # Iterate over each possible end position from start+1 to N
            for end in range(start + 1, N + 1):
                # If the substring from start to end is in the dictionary, mark dp[end] as True
                if s[start:end] in d:
                    dp[end] = True

        # The last element in dp indicates if the entire string can be segmented
        return dp[-1]


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         d = set(wordDict)
#         N = len(s)

#         def dfs(start, s, d, N):
#             if start >= N:
#                 return True

#             for i in range(start, N):
#                 print(s[start:i+1])
#                 if s[start:i + 1] in d:
#                     if dfs(i+1, s, d, N):
#                         return True
#         return dfs(0 s,d,N)

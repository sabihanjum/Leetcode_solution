"""Given a string s, you have to find the number of palindromic subsequences (need not necessarily be distinct) present in the string s. """

class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def countPS(self,s):
        # Code here
        n = len(s)
        md = int(1e9+7)
        dp=[1]*n
        for i in range(1,n):
            cs = 0
            for j in range(i-1,-1,-1):
                tmp = dp[j]
                if(s[i]==s[j]):
                    dp[j]= dp[j]+cs+1
                cs += (tmp%md)
                
        return (sum(dp)%md)
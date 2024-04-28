class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        
        longest = ''
        for i in range(len(s)):                #Find the start of longest substring from index i
            p1 = self.get_palindrome(s, i, i)   # For odd length palindromes
            p2 = self.get_palindrome(s, i, i + 1)  # For even length palindromes
            
            longest = max(longest, p1, p2, key=len)   #Take the maximum between all 3 option
        
        return longest         #Return the longest palindrome string found
    
    def get_palindrome(self, s: str, left: int, right: int) -> str:  #Function to check and add a character
        while left >= 0 and right < len(s) and s[left] == s[right]:  #Checking if both character are same or not
            left -= 1       #Move left pointer towards the right
            right += 1      #Move right pointer towards the middle
        return s[left + 1:right]    #Return the substring which is palindrome

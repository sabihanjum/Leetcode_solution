class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Store the original number
        original = x
        revNum = 0
        
        # Reverse the number
        while x != 0:
            ld = x % 10
            revNum = revNum * 10 + ld
            x //= 10
        
        # Check if the original number is equal to the reversed number
        return original == revNum

"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters."""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []  # Initialize an empty list to store the combinations

        # Mapping of digits to their corresponding characters
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # Helper function for backtracking
        def backtrack(i, curStr):
            # Base case: If the current string length is equal to the length of digits
            if len(curStr) == len(digits):
                res.append(curStr)  # Add the current combination to the result
                return
            
            # Iterate over each character that the current digit maps to
            for c in digitToChar[digits[i]]:
                # Recurse to the next digit with the updated current string
                backtrack(i + 1, curStr + c)

        # Start backtracking only if there are digits to process
        if digits:
            backtrack(0, "")  # Start the backtracking with the first digit and an empty string
        return res  # Return the list of all possible letter combinations

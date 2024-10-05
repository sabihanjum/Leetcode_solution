"""You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string."""

class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Step 1: Iterate through the string 'num' from the end to the start
        for i in range(len(num) - 1, -1, -1):
            # Step 2: Check if the current digit is odd by converting it to an integer and checking modulo 2
            if int(num[i]) % 2 == 1:
                # Step 3: If the digit is odd, return the substring from the start to the current position (inclusive)
                return num[:i + 1]

        # Step 4: If no odd digit is found, return an empty string
        return ""

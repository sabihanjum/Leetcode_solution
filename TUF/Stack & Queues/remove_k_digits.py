"""Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num."""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Remove 'k' digits from the given number 'num' to create the smallest possible number.
        
        Args:
        num (str): The input number represented as a string.
        k (int): The number of digits to remove.

        Returns:
        str: The smallest possible number after removing 'k' digits.
        """
        stack = []  # Monotonic stack to build the smallest number

        # Iterate through each digit in the number
        for c in num:
            # While there are digits left to remove (k > 0) and
            # the current digit is smaller than the last digit in the stack,
            # remove the larger digit to make the number smaller.
            while k > 0 and stack and stack[-1] > c:
                stack.pop()  # Remove the last digit
                k -= 1  # Decrement the count of digits to remove
            
            # Append the current digit to the stack
            stack.append(c)

        # If there are still digits to remove after the loop,
        # remove them from the end of the stack.
        stack = stack[:len(stack) - k]

        # Join the stack into a string to form the result
        res = "".join(stack)

        # Convert to an integer to remove leading zeros, then back to a string.
        # If the result is empty, return "0".
        return str(int(res)) if res else "0"

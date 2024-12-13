"""Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c."""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0  # Initialize the count of valid substrings
        index_a, index_b, index_c = -1, -1, -1  # Initialize pointers for 'a', 'b', 'c'

        # Iterate through the string to find the last occurrences of 'a', 'b', 'c'
        for i, x in enumerate(s):
            if x == 'a':
                index_a = i
            elif x == 'b':
                index_b = i
            else:
                index_c = i

            # If we've found at least 'a', 'b', and 'c', we can form substrings
            if i > 1:  # We need at least 3 characters to form a valid substring
                # The count of substrings ending at index 'i' that contain 'a', 'b', and 'c'
                count += min([index_a, index_b, index_c]) + 1

        return count  # Return the total count of such substrings

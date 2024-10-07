"""Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift."""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Compare the lengths of the strings to ensure they are the same, 
        # which is a prerequisite for one to be a rotation of the other.
        if len(s) != len(goal):
            return False
    
        # Concatenate the string 's' with itself, which covers all possible rotations.
        # If 'goal' is a rotated version of 's', it will be a substring of 's+s'.
        # Check if 'goal' is present within this concatenated string.
        return goal in (s + s)
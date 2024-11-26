"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of open brackets
        stack = []
        
        # A dictionary to map closing brackets to their corresponding opening brackets
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        # Iterate through each character in the string
        for c in s:
            # Check if the character is a closing bracket
            if c in closeToOpen:
                # If the stack is not empty and the top of the stack matches the corresponding opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    # Pop the top element from the stack since it's a valid match
                    stack.pop()
                else:
                    # If there's no match, the string is invalid
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(c)
        
        # After processing all characters, the stack should be empty if the string is valid
        return True if not stack else False

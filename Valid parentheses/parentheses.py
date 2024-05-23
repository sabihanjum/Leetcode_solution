class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize an empty stack to keep track of opening brackets
        dic = {'(': ')', '[': ']', '{': '}'}  # Dictionary to map opening brackets to their corresponding closing brackets

        for c in s:  # Iterate through each character in the input string
            if stack and stack[-1] in "([{" and dic[stack[-1]] == c:
                # If the stack is not empty, the last element in the stack is an opening bracket,
                # and the current character is the matching closing bracket
                stack.pop()  # Pop the last opening bracket from the stack
            else:
                stack.append(c)  # If not, push the current character (opening or closing bracket) onto the stack

        return not stack  # If the stack is empty, all opening brackets have been matched and closed correctly; return True
                        # If the stack is not empty, there are unmatched opening brackets; return False

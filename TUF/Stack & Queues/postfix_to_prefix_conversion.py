"""You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its prefix form."""

class Solution:
    def postToPre(self, s):
        # Stack to hold operands and intermediate results
        stack = []
        i = 0  # Pointer to traverse the postfix expression

        # Iterate through the postfix expression
        while i < len(s):
            # If the current character is an operand (letter or digit), push it onto the stack
            if "a" <= s[i] <= "z" or "A" <= s[i] <= "Z" or "0" <= s[i] <= "9":
                stack.append(s[i])
            else:
                # If the current character is an operator:
                # Check if there are at least two operands on the stack
                if len(stack) < 2:
                    return " "  # Invalid postfix expression

                # Pop two operands from the stack
                t1 = stack.pop()  # First operand (right operand in prefix)
                t2 = stack.pop()  # Second operand (left operand in prefix)

                # Form the prefix expression by placing the operator before the operands
                ans = (s[i] + t2 + t1)

                # Push the resulting prefix expression back onto the stack
                stack.append(ans)

            # Move to the next character
            i += 1

        # After processing the entire expression:
        # If the stack contains exactly one element, it's the final prefix expression
        if len(stack) == 1:
            return stack.pop()
        else:
            # Otherwise, the postfix expression was invalid
            return ""

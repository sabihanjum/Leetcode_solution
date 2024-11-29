"""You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its infix form."""

class Solution:
    def postToInfix(self, expr):
        # Stack to store operands and intermediate infix expressions
        stack = []

        # Traverse each character in the postfix expression
        for char in expr:
            # If the character is an operand (letter or digit), push it onto the stack
            if char.isalpha() or char.isdigit():
                stack.append(char)
            else:
                # If the character is an operator:
                # Check if there are at least two operands on the stack
                if len(stack) < 2:
                    return ""  # Invalid postfix expression
                
                # Pop two operands from the stack
                operand2 = stack.pop()  # Second operand (right side of the operator)
                operand1 = stack.pop()  # First operand (left side of the operator)

                # Form an infix expression by placing the operator between the operands
                infix_expr = "(" + operand1 + char + operand2 + ")"

                # Push the resulting infix expression back onto the stack
                stack.append(infix_expr)

        # After processing all characters, the stack should contain exactly one element
        if len(stack) == 1:
            return stack.pop()  # The final infix expression
        else:
            # If the stack doesn't have exactly one element, the postfix expression was invalid
            return ""

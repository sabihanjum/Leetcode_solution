"""Given an infix expression in the form of string str. Convert this infix expression to postfix expression.

Infix expression: The expression of the form a op b. When an operator is in-between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. Ignore the right associativity of ^."""

class Solution:
    def InfixtoPostfix(self, exp):
        # Initialize an empty string to store the postfix expression
        ans = ""
        # Initialize an empty stack to store operators and parentheses
        stack = []
        # Define operator precedence in a dictionary
        dic = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

        # Iterate through each character in the input expression
        for i in exp:
            # If the character is an operand (alphanumeric), append it to the result
            if i.isalnum():
                ans += i

            # If the character is an opening parenthesis, push it onto the stack
            elif i == '(':
                stack.append(i)

            # If the character is a closing parenthesis
            elif i == ')':
                # Pop from the stack until an opening parenthesis is found
                while stack and stack[-1] != '(':
                    ans += stack.pop()
                # Remove the opening parenthesis from the stack
                stack.pop()

            # If the character is an operator
            else:
                # Pop operators from the stack with higher or equal precedence
                while stack and dic.get(stack[-1], 0) >= dic[i]:
                    ans += stack.pop()
                # Push the current operator onto the stack
                stack.append(i)

        # After iterating through the expression, pop all remaining operators from the stack
        while stack:
            ans += stack.pop()

        # Return the final postfix expression
        return ans

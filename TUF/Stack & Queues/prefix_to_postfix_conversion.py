"""You are given a string that represents the prefix form of a valid mathematical expression. Convert it to its postfix form."""
def preToPost(self, pre_exp):
    # Stack to hold operands and intermediate postfix expressions
    stack = []
    res = ""

    # Traverse the prefix expression from right to left
    for i in range(len(pre_exp) - 1, -1, -1):
        c = pre_exp[i]

        # If the character is an operand (e.g., an alphabet), push it onto the stack
        if c.isalpha():
            stack.append(c)
        else:
            # If the character is an operator, pop two operands from the stack
            s1 = stack.pop()
            s2 = stack.pop()
            
            # Combine them into a postfix expression: operand1 operand2 operator
            res = s1 + s2 + c
            
            # Push the resulting postfix expression back onto the stack
            stack.append(res)
    
    # The final element in the stack is the complete postfix expression
    return stack[-1]

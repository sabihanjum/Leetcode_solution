"""You are given a string S of size N that represents the prefix form of a valid mathematical expression. The string S contains only lowercase and uppercase alphabets as operands and the operators are +, -, *, /, %, and ^.Convert it to its infix form."""

class Solution:
    def preToInfix(self, pre_exp):
        # Stack to hold operands and intermediate expressions
        st = []
        
        # Iterate through the prefix expression from right to left
        for i in range(len(pre_exp)-1, -1, -1):
            c = pre_exp[i]
            
            # If the current character is an operand (i.e., an alphabet), push it onto the stack
            if c.isalpha():
                st.append(c)
            else:
                # If the current character is an operator, pop two operands from the stack
                s1 = st.pop()
                s2 = st.pop()
                
                # Create a new infix expression by surrounding the operands with parentheses
                # and placing the operator between them
                res = '(' + s1 + c + s2 + ')'
                
                # Push the newly formed expression back onto the stack
                st.append(res)
        
        # The final expression (the full infix expression) will be at the top of the stack
        return st[-1]

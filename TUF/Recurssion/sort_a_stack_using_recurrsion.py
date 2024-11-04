"""Given a stack, the task is to sort it such that the top of the stack has the greatest element."""
class Solution:
    # The task is to sort the stack so that the top element is the maximum
    # The function does not return anything; it sorts the stack in place
    def Sorted(self, s):
        # Helper function to sort using recursion
        def helper(s, temp):
            # Base case: If the stack is empty, return
            if len(s) == 0:
                return
            
            # Pop the top element and store it in 'char'
            char = s.pop()
            # Recursively sort the remaining elements
            helper(s, temp)
            
            # Move elements from 's' to 'temp' until we find the right position for 'char'
            while s and s[-1] > char:
                temp.append(s.pop())
            
            # Insert 'char' into the correct sorted position in the stack 's'
            s.append(char)
            
            # Move elements back from 'temp' to 's' to restore the stack order
            while temp:
                s.append(temp.pop())
        
        # Initialize a temporary stack to assist with sorting
        temp = []
        # Call the recursive helper function to sort the stack 's'
        helper(s, temp)

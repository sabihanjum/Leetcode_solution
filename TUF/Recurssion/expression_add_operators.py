"""Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros."""

class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        ans = []  # List to store valid expressions

        def dfs(start: int, prev: int, eval: int, path: list[str]) -> None:
            """
            A depth-first search function to explore all possible expressions.
            
            start: Current index in the string `num`.
            prev: The last operand's value (used for handling multiplication).
            eval: The current value of the expression being built.
            path: List of strings representing the current expression.
            """
            # Base case: If we've reached the end of the string
            if start == len(num):
                # Check if the evaluated expression matches the target
                if eval == target:
                    ans.append(''.join(path))  # Join path as a string and add to result
                return

            # Iterate through all possible substrings starting at `start`
            for i in range(start, len(num)):
                # If the substring starts with '0' and is more than one digit, skip (e.g., "05")
                if i > start and num[start] == '0':
                    return

                # Extract the current substring and convert to an integer
                s = num[start:i + 1]
                curr = int(s)

                # If this is the first number in the expression
                if start == 0:
                    path.append(s)  # Add the number without an operator
                    dfs(i + 1, curr, curr, path)  # Start evaluating with this number
                    path.pop()  # Backtrack
                else:
                    # Try adding each operator ('+', '-', '*') before the current number
                    for op in ['+', '-', '*']:
                        path.append(op + s)  # Add the operator and number
                        
                        if op == '+':
                            # Addition: Add curr to the total evaluation
                            dfs(i + 1, curr, eval + curr, path)
                        elif op == '-':
                            # Subtraction: Subtract curr from the total evaluation
                            dfs(i + 1, -curr, eval - curr, path)
                        else:
                            # Multiplication: Adjust for operator precedence
                            dfs(i + 1, prev * curr, eval - prev + prev * curr, path)
                        
                        path.pop()  # Backtrack by removing the last operation

        # Start the DFS process
        dfs(0, 0, 0, [])
        return ans  # Return the list of valid expressions

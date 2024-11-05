"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses."""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize the output list to store all valid combinations of parentheses
        output = []

        # Helper function for recursive backtracking
        # `left` and `right` track remaining open '(' and close ')' parentheses we can use
        # `stack` represents the balance of open parentheses in the current sequence
        # `cand` is the current candidate string of parentheses being built
        def rec(left, right, stack, cand):
            # Base case: if no more parentheses are left to add, a valid sequence is completed
            if left == right == 0:
                output.append(cand)  # Add the complete sequence to the output list
                return

            # Add an open parenthesis if there are any remaining
            if left > 0:
                rec(left - 1, right, stack + 1, cand + "(")
            
            # Add a closing parenthesis if we have unmatched open parentheses (`stack > 0`)
            if right > 0 and stack > 0:
                rec(left, right - 1, stack - 1, cand + ")")

        # Start the recursive generation with `n` open and `n` close parentheses available
        rec(n, n, 0, "")

        return output

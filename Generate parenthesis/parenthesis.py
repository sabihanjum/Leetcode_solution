class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize an empty list to store the output
        output = []

        # Define a recursive function to generate valid combinations of parentheses
        def rec(left, right, stack, cand):
            # Base case: If both left and right counts are 0, add the candidate to the output
            if left == right == 0:
                output.append(cand)
                return  # Return to exit the current recursive call and go back to the previous level

            # Recursive call for adding '(' if there are remaining left parentheses
            if left > 0:
                rec(left - 1, right, stack + 1, cand + "(")

            # Recursive call for adding ')' if there are remaining right parentheses
            if right > 0 and stack > 0:
                rec(left, right - 1, stack - 1, cand + ")")

        # Start the recursion with equal counts of left and right parentheses, and an empty stack
        rec(n, n, 0, "")

        # Return the list of valid combinations of parentheses
        return output

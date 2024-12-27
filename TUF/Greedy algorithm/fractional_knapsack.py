"""Given two arrays, val[] and wt[], representing the values and weights of items, and an integer capacity representing the maximum weight a knapsack can hold, determine the maximum total value that can be achieved by putting items in the knapsack. You are allowed to break items into fractions if necessary.
Return the maximum value as a double, rounded to 6 decimal places."""

class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, values, weights, w):
        # Initialize an empty list to store value-to-weight ratio along with the index
        stack = []
        # Variable to store the total profit/value obtained
        profit = 0
        # Number of items
        n = len(weights)

        # Calculate the value-to-weight ratio for each item
        for i in range(n):
            percent = values[i] / weights[i]  # Ratio of value to weight
            stack.append([i, percent])  # Append index and ratio to the stack

        # Sort the items by their value-to-weight ratio in descending order
        stack.sort(key=lambda x: x[1], reverse=True)

        # Iterate through the sorted list of items
        for i, prof in stack:
            # If the remaining capacity `w` can accommodate the full weight of the item
            if (w - weights[i]) >= 0:
                w = w - weights[i]  # Reduce the remaining capacity by the item's weight
                profit += values[i]  # Add the full value of the item to the profit
            else:
                # If the item cannot be fully accommodated, take the fractional part
                profit += prof * w  # Add the proportional value to the profit
                break  # Exit the loop as the knapsack is now full

        return profit  # Return the maximum profit obtained

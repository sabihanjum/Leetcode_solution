"""Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price."""

class StockSpanner:
    def __init__(self):
        # Stack to store tuples of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        """
        Function to calculate the stock span for the given price.
        The stock span is the number of consecutive days before (and including)
        the current day for which the price of the stock was less than or equal to
        the current day's price.
        """
        # Initialize the span for the current price as 1 (at least today)
        span = 1

        # While the stack is not empty and the last price in the stack is less than
        # or equal to the current price, pop it and add its span to the current span
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        # Append the current price and its calculated span to the stack
        self.stack.append((price, span))

        # Return the calculated span for the current price
        return span

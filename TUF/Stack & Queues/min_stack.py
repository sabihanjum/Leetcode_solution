"""Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function."""

class MinStack:
    # Initialize two stacks: one for the values and one for tracking minimums.
    def __init__(self):
        self.stack = []       # Main stack to store values.
        self.minStack = []    # Stack to keep track of the minimum value at each point.

    # Push a value onto the stack.
    def push(self, val: int) -> None:
        self.stack.append(val)  # Add the value to the main stack.

        # Calculate the new minimum value. If the minStack is empty, the value itself is the minimum.
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)  # Add the new minimum to the minStack.

    # Remove the top value from the stack.
    def pop(self) -> None:
        self.stack.pop()     # Remove the top value from the main stack.
        self.minStack.pop()  # Remove the corresponding minimum value from the minStack.

    # Retrieve the top value of the stack without removing it.
    def top(self) -> int:
        return self.stack[-1]  # Return the last value in the main stack.

    # Retrieve the minimum value from the stack in constant time.
    def getMin(self) -> int:
        return self.minStack[-1]  # Return the last value in the minStack (current minimum).

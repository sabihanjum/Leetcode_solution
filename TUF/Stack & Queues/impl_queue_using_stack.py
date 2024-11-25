"""Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations."""

class MyQueue:

    def __init__(self):
        # Initialize two stacks, stack1 for pushing elements and stack2 for popping
        self.stack1 = []  # Stack for pushing elements
        self.stack2 = []  # Stack for popping elements

    def push(self, x: int) -> None:
        # Push element x to the end of the queue (add to stack1)
        self.stack1.append(x)

    def pop(self) -> int:
        # Pop the element from the front of the queue
        # If stack2 is empty, move all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Pop the element from stack2 (this is the front of the queue)
        return self.stack2.pop()

    def peek(self) -> int:
        # Get the element at the front of the queue without removing it
        # If stack2 is empty, move all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Return the last element from stack2 (this is the front of the queue)
        return self.stack2[-1]

    def empty(self) -> bool:
        # Check if the queue is empty
        # The queue is empty if both stacks are empty
        return not self.stack1 and not self.stack2

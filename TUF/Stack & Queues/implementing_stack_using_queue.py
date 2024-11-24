"""Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations."""

import collections

class MyStack:
    def __init__(self):
        """
        Initialize the stack using a single queue (`deque` from the `collections` module).
        - `q`: A deque (double-ended queue) that will be used to simulate stack behavior.
        """
        self.q = collections.deque()

    def push(self, x: int) -> None:
        """
        Pushes an element onto the stack.
        - The new element is added to the end of the queue.
        - To maintain stack behavior (LIFO), all elements before the newly added element 
        are moved to the back of the queue, making the new element the front.
        
        Args:
        - x (int): The element to be pushed onto the stack.
        """
        self.q.append(x)  # Add the new element to the queue.
        for _ in range(len(self.q) - 1):  # Rotate all previous elements to the back.
            self.q.append(self.q.popleft())  # Move the front element to the back.

    def pop(self) -> int:
        """
        Removes the top element from the stack.
        - Since the top element is always at the front of the queue (due to the `push` operation),
        the `popleft()` method is used to remove and return it.
        
        Returns:
        - int: The element that was removed from the top of the stack.
        """
        return self.q.popleft()  # Remove and return the front element.

    def top(self) -> int:
        """
        Retrieves the top element of the stack without removing it.
        - The top element is always the front element of the queue.
        
        Returns:
        - int: The top element of the stack.
        """
        return self.q[0]  # Return the front element of the queue.

    def empty(self) -> bool:
        """
        Checks whether the stack is empty.
        
        Returns:
        - bool: `True` if the stack is empty, `False` otherwise.
        """
        return not self.q  # Return `True` if the queue is empty, otherwise `False`.

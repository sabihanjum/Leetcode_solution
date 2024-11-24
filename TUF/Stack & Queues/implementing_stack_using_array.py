"""Write a program to implement a Stack using Array. Your task is to use the class as shown in the comments in the code editor and complete the functions push() and pop() to implement a stack. The push() method takes one argument, an integer 'x' to be pushed into the stack and pop() which returns an integer present at the top and popped out from the stack. If the stack is empty then return -1 from the pop() method.

Note: The input is given in form of queries. Since there are two operations push() and pop(), there is two types of queries as described below:
(i) 1 x   (a query of this type means  pushing 'x' into the stack)
(ii) 2     (a query of this type means to pop an element from the stack and print the popped element)
Input contains separated by space and as described above. """

class MyStack:
    def __init__(self):
        """
        Initialize the stack.
        - `arr`: A fixed-size array to store stack elements (maximum capacity is 100).
        - `size`: Keeps track of the current size of the stack (i.e., the number of elements in the stack).
        """
        self.arr = [0] * 100  # Fixed-size array with an initial capacity of 100.
        self.size = 0  # Initially, the stack is empty.

    def push(self, data):
        """
        Pushes an element onto the stack.
        - The element `data` is added at the current `size` index, 
        and the `size` is incremented to reflect the addition.
        
        Args:
        - data: The element to be added to the stack.
        """
        self.arr[self.size] = data  # Add the new element to the current index.
        self.size += 1  # Increase the size to reflect the addition.

    def pop(self):
        """
        Removes the top element from the stack and returns it.
        - If the stack is empty (`size <= 0`), return -1 as an error indicator.
        - Otherwise, decrement the `size` and return the last added element.
        
        Returns:
        - The element that was removed from the top of the stack, or -1 if the stack is empty.
        """
        if self.size <= 0:  # Check if the stack is empty.
            return -1  # Return -1 to indicate an empty stack.
        
        self.size -= 1  # Decrease the size to remove the top element.
        return self.arr[self.size]  # Return the last element from the stack.

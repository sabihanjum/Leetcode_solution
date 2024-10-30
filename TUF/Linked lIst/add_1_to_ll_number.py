"""You are given a linked list where each element in the list is a node and have an integer data. 
You need to add 1 to the number formed by concatinating all the list node numbers together and return the 
head of the modified linked list. Note: The head represents the first element of the given array."""

class Solution:
    # Recursive function to add one to the linked list
    def addOneRec(self, head):
        # Base case: if it's the last node
        if not head.next:
            # Calculate carry after adding 1 to the last node
            carry = (head.data + 1) // 10
            # Update the last node's data after adding 1
            head.data = (head.data + 1) % 10
            # Return the carry to the previous node
            return carry
        
        # Recursive call to add one to the next node
        temp = self.addOneRec(head.next)
        # Calculate carry for the current node
        carry = (head.data + temp) // 10
        # Update current node's data with the result
        head.data = (head.data + temp) % 10
        
        return carry
            
    # Main function to add one to the number represented by the linked list
    def addOne(self, head):
        # Edge case: if the list has only one node
        if not head.next:
            carry = (head.data + 1) // 10
            head.data = (head.data + 1) % 10
        else:
            # Start recursion from the head node and get carry for the first node
            temp = self.addOneRec(head)
            carry = temp
        
        # If there's a carry remaining, create a new head node with carry
        if carry:
            temp = Node(1)  # New node to hold the carry
            temp.next = head  # Make current head the next of new node
            head = temp  # Update head to the new node
        
        return head

"""Given a Linked List, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked lists is in sorted order.
Flatten the Link List so all the nodes appear in a single level while maintaining the sorted order.

Note: The flattened list will be printed using the bottom pointer instead of the next pointer. Look at the 
printList() function in the driver code for more clarity."""

def flatten(self, root):
    # Initialize a pointer 'temp' to traverse the list starting from the root
    temp = root

    # First loop to rearrange the next nodes into bottom nodes
    while temp is not None:
        next_node = None
        # If there is a next node, store it and set temp.next to None
        if temp.next is not None:
            next_node = temp.next
            temp.next = None

        # Move to the bottom-most node in the current list
        while temp.bottom is not None:
            temp = temp.bottom

        # Link the previously stored next_node to the bottom-most node
        temp.bottom = next_node

        # Move to the next bottom node to continue the process
        temp = temp.bottom

    # Reset 'temp' back to the root for sorting
    temp = root

    # Second loop to sort the flattened list using bubble sort logic
    while temp is not None:
        # Initialize a pointer 'curr' to traverse from the bottom node
        curr = temp.bottom
        # Inner loop to compare each node with temp and sort data in ascending order
        while curr is not None:
            # If the current node's data is less than temp, swap the values
            if temp.data > curr.data:
                temp.data, curr.data = curr.data, temp.data
            # Move to the next bottom node
            curr = curr.bottom
        # Move to the next bottom node for outer loop
        temp = temp.bottom

    # Return the modified root node
    return root

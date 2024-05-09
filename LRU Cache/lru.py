class Node:
  # Define a class Node to represent each node in the linked list.
  def __init__(self, key: int, value: int):
    # Initialize the Node with a key, value, prev pointer, and next pointer.
    self.key = key
    self.value = value
    self.prev = None
    self.next = None

class LRUCache:
  # Define a class LRUCache for implementing the LRU cache.
  def __init__(self, capacity: int):
    # Initialize the LRUCache with a specified capacity.
    self.capacity = capacity
    # Dictionary to store key-value pairs for O(1) access.
    self.keyToNode = {}
    # Initialize a dummy head and a dummy tail for the linked list.
    self.head = Node(-1, -1)
    self.tail = Node(-1, -1)
    # Join the head and tail to create an empty linked list.
    self.join(self.head, self.tail)

  def get(self, key: int) -> int:
    # Retrieve the value corresponding to a given key.
    if key not in self.keyToNode:
      return -1
    # If key exists, move the corresponding node to the head (most recently used).
    node = self.keyToNode[key]
    self.remove(node)
    self.moveToHead(node)
    return node.value

  def put(self, key: int, value: int) -> None:
    # Insert or update the value associated with a given key.
    if key in self.keyToNode:
      # If key exists, update the value and move the node to the head.
      node = self.keyToNode[key]
      node.value = value
      self.remove(node)
      self.moveToHead(node)
      return
    # If the cache is full, remove the least recently used node (tail node).
    if len(self.keyToNode) == self.capacity:
      lastNode = self.tail.prev
      del self.keyToNode[lastNode.key]
      self.remove(lastNode)
    # Insert the new node at the head and update the dictionary.
    self.moveToHead(Node(key, value))
    self.keyToNode[key] = self.head.next

  def join(self, node1: Node, node2: Node):
    # Helper function to join two nodes in the linked list.
    node1.next = node2
    node2.prev = node1

  def moveToHead(self, node: Node):
    # Move a node to the head of the linked list.
    self.join(node, self.head.next)
    self.join(self.head, node)

  def remove(self, node: Node):
    # Remove a node from the linked list.
    self.join(node.prev, node.next)

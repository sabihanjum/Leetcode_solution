"""Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity."""

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity):
        """
        Initialize the LFU Cache with a given capacity.
        :param capacity: Maximum number of items the cache can hold.
        """
        self.capacity = capacity  # Max capacity of the cache
        self.min_frequency = 0  # Tracks the minimum frequency of keys in the cache
        self.current_size = 0  # Tracks the current number of keys in the cache
        self.frequency_list = defaultdict(OrderedDict)  # Group keys by frequency (OrderedDict maintains order of insertion)
        self.key_node = {}  # Maps keys to their position in frequency_list
        self.frequency = {}  # Stores the frequency and value for each key: {key: [frequency, value]}

    def get(self, key):
        """
        Get the value of the key if it exists in the cache. 
        Update its frequency as it's been accessed.
        :param key: Key to be accessed.
        :return: Value of the key if it exists, otherwise -1.
        """
        if key not in self.key_node:
            return -1  # Return -1 if key is not in the cache

        # Get the current frequency of the key
        key_freq = self.frequency[key][0]

        # Remove the key from its current frequency group
        del self.frequency_list[key_freq][key]

        # Increment the key's frequency
        self.frequency[key][0] += 1

        # Add the key to the new frequency group
        self.frequency_list[self.frequency[key][0]][key] = None
        self.key_node[key] = next(iter(self.frequency_list[self.frequency[key][0]]))

        # Update min_frequency if the old frequency group is empty
        if not self.frequency_list[self.min_frequency]:
            self.min_frequency += 1

        # Return the value associated with the key
        return self.frequency[key][1]

    def put(self, key, value):
        """
        Add a key-value pair to the cache. If the cache reaches capacity,
        evict the least frequently used key.
        :param key: Key to be added or updated.
        :param value: Value associated with the key.
        """
        if self.capacity <= 0:
            return  # Do nothing if cache capacity is 0 or negative

        if key in self.key_node:
            # If the key is already in the cache, update its value and frequency
            self.frequency[key][1] = value
            self.get(key)  # Access the key to update its frequency
            return

        # If the cache is full, evict the least frequently used key
        if self.current_size == self.capacity:
            # Find the least frequently used key in the min_frequency group
            min_freq_key = next(iter(self.frequency_list[self.min_frequency]))
            # Remove the key from the cache and frequency tracking structures
            del self.key_node[min_freq_key]
            del self.frequency[min_freq_key]
            del self.frequency_list[self.min_frequency][min_freq_key]
            self.current_size -= 1  # Decrement the current cache size

        # Add the new key to the cache
        self.current_size += 1
        self.min_frequency = 1  # Reset min_frequency to 1 for the new key
        self.frequency_list[self.min_frequency][key] = None  # Add key to the frequency list
        self.key_node[key] = next(iter(self.frequency_list[self.min_frequency]))
        self.frequency[key] = [1, value]  # Initialize the key's frequency and value

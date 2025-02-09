"""Problem statement
Ninja has to implement a data structure ”TRIE” from scratch. Ninja has to complete some functions.

1) Trie(): Ninja has to initialize the object of this “TRIE” data structure.

2) insert(“WORD”): Ninja has to insert the string “WORD”  into this “TRIE” data structure.

3) countWordsEqualTo(“WORD”): Ninja has to return how many times this “WORD” is present in this “TRIE”.

4) countWordsStartingWith(“PREFIX”): Ninjas have to return how many words are there in this “TRIE” that have the string “PREFIX” as a prefix.

5) erase(“WORD”): Ninja has to delete one occurrence of the string “WORD” from the “TRIE”.
Note:

1. If erase(“WORD”) function is called then it is guaranteed that the “WORD” is present in the “TRIE”.

2. If you are going to use variables with dynamic memory allocation then you need to release the memory associated with them at the end of your solution.
Can you help Ninja implement the "TRIE" data structure?"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_count = 0  # Counts occurrences of a word
        self.prefix_count = 0  # Counts occurrences of words with a given prefix

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        node.word_count += 1

    def countWordsEqualTo(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.word_count

    def countWordsStartingWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.prefix_count

    def erase(self, word):
        node = self.root
        stack = []  # To track the path
        
        for char in word:
            if char not in node.children:
                return  # Word does not exist in Trie
            stack.append((node, char))
            node = node.children[char]
        
        if node.word_count > 0:
            node.word_count -= 1
        else:
            return  # Word does not exist in Trie
        
        # Reduce prefix counts and clean up unnecessary nodes
        while stack:
            parent, char = stack.pop()
            parent.children[char].prefix_count -= 1
            if parent.children[char].prefix_count == 0:
                del parent.children[char]

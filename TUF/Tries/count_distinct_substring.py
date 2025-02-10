"""Given a string 'S', you are supposed to return the number of distinct substrings(including empty substring) of the given string. You should implement the program using a trie.

Note :
A string ‘B’ is a substring of a string ‘A’ if ‘B’ that can be obtained by deletion of, several characters(possibly none) from the start of ‘A’ and several characters(possibly none) from the end of ‘A’. 

Two strings ‘X’ and ‘Y’ are considered different if there is at least one index ‘i’  such that the character of ‘X’ at index ‘i’ is different from the character of ‘Y’ at index ‘i’(X[i]!=Y[i])."""

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        node = self.root
        count = 0
        for char in s:
            if char not in node.children:
                node.children[char] = TrieNode()
                count += 1  # New substring found
            node = node.children[char]
        return count

def countDistinctSubstrings(s):
    trie = Trie()
    total_count = 1  # Counting the empty substring
    
    for i in range(len(s)):
        total_count += trie.insert(s[i:])
    
    return total_count

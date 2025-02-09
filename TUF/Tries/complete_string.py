"""Ninja developed a love for arrays and strings so this time his teacher gave him an array of strings, ‘A’ of size ‘N’. Each element of this array is a string. The teacher taught Ninja about prefixes in the past, so he wants to test his knowledge.

A string is called a complete string if every prefix of this string is also present in the array ‘A’. Ninja is challenged to find the longest complete string in the array ‘A’.If there are multiple strings with the same length, return the lexicographically smallest one and if no string exists, return "None".

Note :
String ‘P’ is lexicographically smaller than string ‘Q’, if : 

1. There exists some index ‘i’ such that for all ‘j’ < ‘i’ , ‘P[j] = Q[j]’ and ‘P[i] < Q[i]’. E.g. “ninja” < “noder”.

2. If ‘P’ is a prefix of string ‘Q’, e.g. “code” < “coder”.
Example :
N = 4
A = [ “ab” , “abc” , “a” , “bp” ] 

Explanation : 

Only prefix of the string “a” is “a” which is present in array ‘A’. So, it is one of the possible strings.

Prefixes of the string “ab” are “a” and “ab” both of which are present in array ‘A’. So, it is one of the possible strings.

Prefixes of the string “bp” are “b” and “bp”. “b” is not present in array ‘A’. So, it cannot be a valid string.

Prefixes of the string “abc” are “a”,“ab” and “abc” all of which are present in array ‘A’. So, it is one of the possible strings.

We need to find the maximum length string, so “abc” is the required string."""

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True
    
    def has_all_prefixes(self, word):
        node = self.root
        for char in word:
            if char not in node.children or not node.children[char].end_of_word:
                return False
            node = node.children[char]
        return True

def completeString(n: int, a: List[str]) -> str:
    trie = Trie()
    for word in a:
        trie.insert(word)
    
    longest = "None"
    
    for word in a:
        if trie.has_all_prefixes(word):
            if longest == "None" or len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                longest = word
    
    return longest

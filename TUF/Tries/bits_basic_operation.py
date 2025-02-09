"""Geek is learning data structures. He wants to learn the trie data structure, but there are a few bit's prerequisites that he must first understand.

Given three bit manipulations functions: XOR, check and setBit.

In XOR function you are given two integers n and m return the xor of n and m.

In check function you are given two integer a and b return 1 if ath bit (1-indexed) of b is set otherwise return 0.

In setBit function you are given two integer c and d, set the cth bit (0-indexed) of d if not yet set ."""
class Solution:
    def XOR(self, n, m):
        return n ^ m
    def check(self, a, b):
        return (b >> (a-1)) & 1
    def setBit(self, c, d):
        return d | (1 << c)
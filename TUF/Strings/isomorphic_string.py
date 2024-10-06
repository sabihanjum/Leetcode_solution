"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the 
order of characters. No two characters may map to the same character, but a character may 
map to itself."""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Dictionaries to map characters from s to t and from t to s
        mapST, mapTS = {}, {}

        # Iterate over both strings s and t simultaneously using zip
        for c1, c2 in zip(s, t):
            # If c1 is already mapped in mapST and it doesn't map to c2, return False
            # If c2 is already mapped in mapTS and it doesn't map to c1, return False
            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
                return False

            # Map c1 to c2 in mapST (mapping s to t)
            # Map c2 to c1 in mapTS (mapping t to s)
            mapST[c1] = c2
            mapTS[c2] = c1

        # If all characters are mapped correctly, return True
        return True

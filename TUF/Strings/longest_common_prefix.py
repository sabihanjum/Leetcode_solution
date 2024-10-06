"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize an empty string to store the result (longest common prefix)
        res = ""

        # Check if the list of strings is empty, return empty string if true
        if not strs:
            return res

        # Loop through each character index of the first string in the list
        for i in range(len(strs[0])):
            # Compare the character at index 'i' of each string in the list
            for s in strs:
                # If index 'i' is out of bounds for any string or characters do not match, return the result
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            # If characters match for all strings at index 'i', add the character to the result
            res += strs[0][i]
        
        # Return the longest common prefix
        return res

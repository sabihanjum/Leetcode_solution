"""Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Initialize variables
        words = []  # This will store the words in the string
        word = ""   # Temporary variable to build each word

        # Step 2: Iterate over the string 's' character by character
        for char in s:
            if char != ' ':
                # If the character is not a space, add it to the current word
                word += char
            else:
                # If a space is encountered, the current word is complete
                if word:
                    words.append(word)  # Add the word to the list of words
                    word = ""  # Reset for the next word

        # Step 3: Add the last word if the loop ends and there is a word
        if word:
            words.append(word)

        # Step 4: Reverse the list of words
        reversed_words = []
        for i in range(len(words) - 1, -1, -1):
            reversed_words.append(words[i])

        # Step 5: Rebuild the string by concatenating the reversed words with spaces
        result = ""
        for word in reversed_words:
            result += word + " "

        # Step 6: Return the final result after stripping any trailing space
        return result.strip()

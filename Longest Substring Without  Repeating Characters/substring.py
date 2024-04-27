class Solution:       
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0           #start is the beginning of current substring and maxlength
        usedChar = {}                   #usedChar stored all character in string and it's corresponding position in string
        for i in range(len(s)):         #for each char in string           
            if s[i] in usedChar and start <= usedChar[s[i]]:     #if the char has been used before
                start = usedChar[s[i]] + 1             #start from next one
            else:
                maxLength = max(maxLength, i-start+1)  #update the maxLength when find a new longest subsstring

            usedChar[s[i]] = i     #mark this char as used with its last position

        return maxLength           #return the maximum length of all substring

        
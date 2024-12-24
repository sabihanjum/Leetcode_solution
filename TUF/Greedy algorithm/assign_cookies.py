"""Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number."""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        Function to find the maximum number of content children given greed factors and cookie sizes.
        :param g: List[int] - List of greed factors of the children
        :param s: List[int] - List of sizes of cookies
        :return: int - Maximum number of content children
        """
        # Step 1: Sort greed factors (g) and cookie sizes (s) in ascending order
        g.sort()
        s.sort()

        i = j = 0  # Pointers for greed factors (i) and cookie sizes (j)
        
        # Step 2: Iterate through the greed factors
        while i < len(g):
            # Find a cookie that satisfies the current child's greed factor
            while j < len(s) and g[i] > s[j]:
                j += 1  # Move to the next cookie
            
            # If no more cookies are available, break the loop
            if j == len(s):
                break
            
            # Step 3: Assign the current cookie to the child
            i += 1  # Move to the next child
            j += 1  # Move to the next cookie
        
        # Step 4: Return the count of content children
        return i

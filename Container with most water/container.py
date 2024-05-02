class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0                 #Poinnter to left side container
        p2 = len(height) - 1    #Pointer to right side container 
        max_area = 0            #Maximum area so far
        while p1 != p2:         #One pointer will reach the one point of array
            if height[p1] > height[p2]:   #If the height is greater than p1 to p2
                area = height[p2] * (p2 - p1)   #Calculate the current area with width
                p2 -= 1     #Move pointer to right side with smaller height
            else:
                area = height[p1] * (p2 - p1)   #The same as above with p1
                p1 += 1      #Move pointer to left side with smaller height
            if area > max_area: max_area = area   #Update maximum area if necessary
        return max_area     #Return the maximum area
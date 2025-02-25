"""Given start, end and an array arr of n numbers. At each step, start is multiplied with any number in the array and then mod operation with 100000 is done to get the new start.

Your task is to find the minimum steps in which end can be achieved starting from start. If it is not possible to reach end, then return -1."""

from typing import List
import math
from collections import deque
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        
        if start==end:
            return 0
        
        dist=[math.inf for i in range(100000)]
        q=deque()
        q.append([0,start])

        while (q):
            step,num=q.popleft()

            for ele in arr:
                new=(num*ele)%100000
                
                if step+1<dist[new]:
                    dist[new]=step+1
                    if new==end:
                        return step+1
                    q.append([step+1,new])
                
                    
        return -1
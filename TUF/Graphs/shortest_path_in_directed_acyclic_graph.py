"""Given a Directed Acyclic Graph of V vertices from 0 to n-1 and a 2D Integer array(or vector) edges[ ][ ] of length E, where there is a directed edge from edge[i][0] to edge[i][1] with a distance of edge[i][2] for all i.

Find the shortest path from src(0) vertex to all the vertices and if it is impossible to reach any vertex, then return -1 for that vertex."""

from typing import List
import math

class Solution:
    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        
        adjL = [[] for i in range(V)]
        for i in edges:
            src = i[0]
            dest = i[1]
            dist = i[2]

            adjL[src].append([dest, dist])

        # print("adjL", adjL)

        def TopoSort():
            st = []
            ans=[]
            inDegree = [0 for i in range(V)]

            for i in range(len(adjL)):
                for j in adjL[i]:
                    inDegree[j[0]]+=1
                    
            for i in range(len(inDegree)):
                if inDegree[i]==0:
                    st.append(i)
            
            while (st):
                ele=st.pop()
                ans.append(ele)
                for (n,d) in adjL[ele]:
                    inDegree[n]-=1
                    if inDegree[n]==0:
                        st.append(n)
                    
    
            return ans[::-1]
    
        stack = TopoSort()
        # print("stack", stack)

        for i in range(len(stack)-1, -1, -1):
            if stack[i] == 0:
                stack = stack[:i+1]
                break

        # print("stack", stack)

        dist = [math.inf for i in range(V)]
    
        l = len(stack)
        while (stack):
            ele = stack.pop()
            if len(stack) == l-1:
                dist[ele] = 0

            for (n, d) in adjL[ele]:
                dist[n] = min(dist[n], dist[ele]+d)

        for i in range(V):
            if dist[i] == math.inf:
                dist[i] = -1
        return dist


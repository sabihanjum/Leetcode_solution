"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array."""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        ourDegree = {i:0 for i in range(numCourses)}
        for i,j in prerequisites:
            graph[i].append(j)
            ourDegree[j] += 1
        
        queue = deque()
        for i in ourDegree:
            if ourDegree[i] == 0:
                queue.append(i)
                
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for i in graph[node]:
                ourDegree[i] -= 1
                if ourDegree[i] == 0:
                    queue.append(i)
        if len(result) != numCourses: return []
        return result[::-1]
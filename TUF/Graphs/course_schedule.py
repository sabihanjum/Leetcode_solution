"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false."""

from enum import Enum


class State(Enum):
    kInit = 0
    kVisiting = 1
    kVisited = 2


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        states = [State.kInit] * numCourses

        for v, u in prerequisites:
            graph[u].append(v)

        def hasCycle(u: int) -> bool:
            if states[u] == State.kVisiting:
                return True
            if states[u] == State.kVisited:
                return False
            states[u] = State.kVisiting
            if any(hasCycle(v) for v in graph[u]):
                return True
            states[u] = State.kVisited
            return False

        return not any(hasCycle(i) for i in range(numCourses))
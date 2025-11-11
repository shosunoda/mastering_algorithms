from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = [[] for _ in range(numCourses)]
        
        for course, prereq in prerequisites:
            self.graph[prereq].append(course)
        self.visited = set()
        self.visiting = set()

        def dfs(node: int):
            if node in self.visiting:
                return False
            if node in self.visited:
                return True
            self.visiting.add(node)
            for neighbor in self.graph[node]:
                if not dfs(neighbor):
                    return False
            self.visiting.remove(node)
            self.visited.add(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
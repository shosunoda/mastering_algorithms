from typing import List, Tuple
from collections import deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]

        for src, dst, distance in roads:
            graph[src].append((dst, distance))
            graph[dst].append((src, distance))

        visited = set()
        q = deque([1])
        visited.add(1)

        ans = float("inf")

        while q:
            cur = q.popleft()
            for neigh, cost in graph[cur]:
                ans = min(ans, cost)
                if neigh not in visited:
                    visited.add(neigh)
                    q.append(neigh)

        return ans
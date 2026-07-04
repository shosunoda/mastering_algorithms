from typing import List, Tuple
import heapq

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
        max_edge = 0

        for src, dst, cost in edges:
            if online[src] and online[dst]:
                graph[src].append((dst, cost))
                max_edge = max(max_edge, cost)
        def can(score: int) -> bool:
            shortest_cost = {}
            heap = [(0, 0)]  

            while heap:
                cost_so_far, node = heapq.heappop(heap)
                if node in shortest_cost:
                    continue
                shortest_cost[node] = cost_so_far

                if node == n - 1:
                    return cost_so_far <= k
                for nei, edge_cost in graph[node]:
                    if edge_cost < score:
                        continue

                    new_cost = cost_so_far + edge_cost
                    if new_cost <= k and nei not in shortest_cost:
                        heapq.heappush(heap, (new_cost, nei))
            return False

        left, right = 0, max_edge
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
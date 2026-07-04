from typing import List, Tuple
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph: List[List[Tuple[int, float]]] = [[] for x in range(n)]
        for (src, dst), cost in zip(edges, succProb):
            graph[src].append((dst, cost))
            graph[dst].append((src, cost))
        #  and now we want o return the maximum probability og going froms tart to end 
        # 
        # this i just the opposite of djikstars, no we we want to maximiimse the probability 
        # uh cant we just do a negative heap, we can do e nagetiave heap
        # because once we pop it, we can be sure that value is finalised 
        priorityq = [(-1, start_node)]
        visited = set()
        while priorityq:
            cur_prob, cur_cell = heapq.heappop(priorityq)
            if cur_cell == end_node:
                return abs(cur_prob)
            visited.add(cur_cell)
            for neigh, next_prob, in graph[cur_cell]: 
                if neigh in visited:
                    continue
                potential_prob = cur_prob * next_prob
                heapq.heappush(priorityq, (potential_prob, neigh))
        return 0

            

        
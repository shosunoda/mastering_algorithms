from typing import Tuple, List
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #  n inteersectiosn 
        # continuous 
        # 
        #  number of ways to ge tthe shortest amount of time
        #  we know the way to get the shortest amount of time froms rc to dstinations, can be derived from djikstars right
        # how do we want to find the number of shortest paths from there then
        # if we can count the number of ways to reach node b, and c, and to reac hde node d
        # we need to ghtough b and c for thosrest path, its just those 2 paths right 
        # but then the question is how do you count the number of ways to reach a path
        graph: List[List[Tuple[int, int]]] = [[] for x in range(n)]
        MOD = 10**9 + 7
        for src, dst, cost in roads:
            graph[src].append((dst, cost))
            graph[dst].append((src, cost))
        
        priorityq = [(0, 0)]
        min_cost = [float('inf')] * n
        min_cost[0] = 0 
        path_count = [0] * n
        path_count[0] = 1
        while priorityq:
            cur_cost, cur_node = heapq.heappop(priorityq)
            # if cur_cost > min_cost[cur_node]:
            #     continue
            for neigh, neigh_cost in graph[cur_node]: 

                new_cost = neigh_cost + cur_cost
                if new_cost > min_cost[neigh]:
                    continue
                # this avoids cycles aand doing retrvaersals because we ignore paths longer than the oens we have already explored 
                if new_cost < min_cost[neigh]: 
                    path_count[neigh] = path_count[cur_node]
                    min_cost[neigh] = new_cost
                    heapq.heappush(priorityq, (new_cost, neigh))
                elif new_cost == min_cost[neigh]:
                    path_count[neigh] = (path_count[cur_node] + path_count[neigh]) % MOD
        return path_count[n - 1]


from collections import deque
from typing import Tuple, List 

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #  we are given heights, which is a 2d array of size rows x collumns
        # which is the same thing sa a 2d grid 
        #  got it
        #  we start in the top left cell denoted by 0, 0
        # we want to go to the bototm right cell which is denoted by rows -1, col -1 
        # we want to find the mionimum effort 
        # which is the absolute difference in heights between two consecutive cells of the route 
        # 
        # wel
        rows, cols = len(heights), len(heights[0])

        lowest_value = min(min(row) for row in heights)
        highest_value = max(max(row) for row in heights)
        right = highest_value - lowest_value
        left = 0 
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def feasible(difference: int) -> bool:
            # 
            # 
            # this is jsut going be dfs 
            to_visit = deque()
            to_visit.append((0, 0))
            visited = set()
            visited.add((0, 0))
            while to_visit: 
                cur_cell = to_visit.pop()
                cur_row, cur_col = cur_cell
                if cur_row == (len(heights) - 1) and cur_col == (len(heights[0]) -1):
                    return True
                cur_distance = heights[cur_cell[0]][cur_cell[1]]
                for dif_row, dif_col in directions: 
                    dr = cur_row + dif_row
                    dc = cur_col + dif_col
                    if (dr, dc) in visited:
                        continue
                    if dr < 0 or dr >= len(heights) or dc < 0 or dc >= len(heights[0]) or (abs(heights[dr][dc] - cur_distance )) > difference:
                        continue 
                    to_visit.append((dr, dc))
                    visited.add((dr, dc))
            return False
        while left < right:
            mid = (left + right) // 2
            if feasible(mid): 
                right = mid 
            else:
                left = mid + 1
        return left
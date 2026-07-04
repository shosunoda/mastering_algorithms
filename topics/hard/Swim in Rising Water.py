from typing import List, Tuple
from collections import deque

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        left = grid[0][0]
        right = max(max(row) for row in grid)
        directions: List[Tuple[int, int]] = [ (0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])


        def feasible(time: int) -> bool:
            queue = deque()
            queue.append((0, 0))
            visited = set()
            visited.add((0, 0))
            while queue: 
                cur_cell = queue.pop()
                cur_row, cur_col = cur_cell
                if cur_row == (rows - 1) and cur_col == (cols - 1):
                    return True
                visited.add((cur_row, cur_col))
                cur_distance = grid[cur_row][cur_col]
                for dr, dc in directions: 
                    nr, nc = cur_row + dr, cur_col + dc
                    if (nr, nc) in visited:
                        continue
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] > time:
                        continue
                    queue.append((nr, nc))
            return False
        
        while left < right: 
            mid = (left + right) // 2
            if feasible(mid):
                right = mid 
            else:
                left = mid + 1
        return left

                

        
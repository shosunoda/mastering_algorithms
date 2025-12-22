from collections import deque
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # bfs kinda 
        # the first layer you have to extract the first letter, and then you do bfs from there to sea ny adjcents cahracters anything, a
        # if they dont return False
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[i]
            ):
                return False

            temp = board[r][c]
            board[r][c] = "#"   # mark visited

            found = (
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1)
            )

            board[r][c] = temp  # backtrack
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False




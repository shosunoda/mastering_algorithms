from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(index, path, total):
            # base cases
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            if index >= len(candidates):
                return

            path.append(candidates[index])
            dfs(index + 1, path, total + candidates[index])
            path.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            dfs(index + 1, path, total)  
            return

        dfs(0, [], 0)
        return result

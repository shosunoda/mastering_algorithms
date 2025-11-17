from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # we need to ensure its unique solutions right
        # i think this can be modelled thorugh recursion tree once agian
        # at each index, you have two choices
        # you either use this index again add it the target, or you skip to the next index
        # we guarnetee this will lead to unique frequencies because you will not end up in the same traverls
        # from two differen paths
        # and with the addition that all candiates are unique, you cant form the same path despite starting from different elements
        result = []
        def dfs(index, current):
            if sum(current) == target:
                result.append(current[:])
                return
            if index == len(candidates) or sum(current) > target:
                return 
            current.append(candidates[index])
            take_path = dfs(index, current)
            current.pop()
            next_path = dfs(index + 1, current)
            return
        dfs(0, [])
        return result

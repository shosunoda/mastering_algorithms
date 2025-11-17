from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        # theres basically, you have a choice every signle number
        # to either inlclude it or excluse 
        # this ends up becomign a tree/recursive
        # so dont include 1, now we have another to include 2 or not to include 2, and then another choice to include 3 or not to include 3
        # so this can be modelled through recursion/dfs 
        # where we try and explore eahc path until ew reach the end of the the aray
        # so the base case would be the end of the array 
        # and we can also include backttracking in this
        # because evreytime we explore a path, we can just pop the latest element and explore the next adjacent
        # let me implement thi snow
        def dfs(index, path):
            if index == len(nums):
                result.append(path[:])
                return
            path.append(nums[index])
            dfs(index + 1, path)
            path.pop()
            dfs(index + 1, path)
            return 
        dfs(0, [])
        return result
        
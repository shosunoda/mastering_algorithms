from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(index):
            if index >= len(nums):
                return 0
            if index in cache:
                return cache[index]
            cur = nums[index]
            cache[index] = max(dfs(index + 1) , cur + dfs(index + 2))
            return cache[index]
        return dfs(0)

        
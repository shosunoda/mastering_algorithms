from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        #[2,3,1,1,4]
        # 
        l = r = 0
        jumps = 0
        furthest = 0
        while r < len(nums) - 1:
            for hop in range(l, r + 1):
                furthest = max(furthest, hop + nums[hop])
            l = r + 1
            r = furthest
            jumps += 1
        return jumps
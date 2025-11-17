from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # how is this ahard question
        # weo have return an array of len(nums) - k + 1 values
        # right 
        # i dont understand whats hard about this 
        # i mean so apparenrlt the realisation is that once a number ias passed
        # if its its a later alter index and also alrger, then we will never ever use that value ever again 
        queue = deque()
        result = []
        left = 0
        for right in range(len(nums)):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)
            if queue[0] < left:
                queue.popleft()
            if (right + 1) >= k:
                result.append(nums[queue[0]])
                left += 1
        return result

        
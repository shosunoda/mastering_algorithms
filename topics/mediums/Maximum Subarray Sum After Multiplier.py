import math
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        def divide(x):
            if x >= 0:
                return x // k
            else:
                return -( (-x) // k)
        def kadane(transform):
            NEG = -10**38
            normal = 0 
            doing = NEG
            done = NEG
            ans = NEG
            for x in nums:
                y = transform(x)
                old_normal = normal
                old_doing = doing 
                old_done = done

                normal = max(old_normal +x, x)
                doing = max(old_doing + y, old_normal + y, y)
                done = max(old_done + x, old_doing + x)
                ans = max(ans, doing, done)
            return ans 
        multiply_ans = kadane(lambda x: x *k)
        divide_ans = kadane(divide)
        return max(multiply_ans, divide_ans)
        
        
        
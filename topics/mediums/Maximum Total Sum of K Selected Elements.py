class Solution: 
        def maxSum(self, nums: list[int], k: int, mul: int) -> int:
            nums.sort(reverse = True)
            ans = 0 
            for i in range(k):
                ans += nums[i] *max(1, mul - i)
            return ans
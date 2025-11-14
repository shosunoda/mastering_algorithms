from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = sum(nums)
        expected_sum = (len(nums) *(len(nums) + 1)) // 2
        return expected_sum - actual_sum
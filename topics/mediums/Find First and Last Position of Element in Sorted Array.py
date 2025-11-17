from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # what is one we can do this, i plan on creating tow different helper functions to do this 
        # what would the difference be etween these two binary search functiosn 
        # the difference is that we would have bias in our binary search, in the usual binary search, if we encounter a value 
        # that we want we would return true, in this one, we want to find the firstl/ast occurence
        # so lets say we want to find the starting occureence of a value using binary search 
        # the best way to do this is probably to always ptu the bias to search the left hand side even when we find a value that equals our target, such that bhinary left tends to the left # vice versa for the ending point
        if not nums:
            return [-1, -1]
        start, end = self.findStart(nums, target), self.findEnd(nums, target)
        if start < 0 or start >= len(nums) or end < 0 or end >= len(nums):
            return [-1, -1 ]
        if nums[start] != target or nums[end] != target:
            return [-1, -1 ]
        return [start, end]

    def findStart(self, nums, target):
        left = 0 
        right = len(nums) - 1
        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def findEnd(self, nums, target):
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right 

        
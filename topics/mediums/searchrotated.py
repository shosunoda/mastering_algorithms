from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #[4,5,6,7,0,1,2]
        # everytime im given an array with sorted values as well as the condtion of it being log
        # it screams binary search 
        # [4,5,6,7,0,1,2]
        # however, we are also given the contrains that its left rotated, which means the nums 
        # got shifted to the left by 3 
        # i mean for us, this means that there are 2 sorted search places 
        # 
        # 4,5,6   7. ,0,1,2
        # lets say we are trying to find 0 right
        # we see that 0 is greater than 7
        # however, we also see nums
        # so target is smaller than 7, so what, which side of the array can we actually remove
        # 
        # we go the right side because 
        #.  [4,5,6,7,0,1,2]
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1


            else:

                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1 

        return - 1

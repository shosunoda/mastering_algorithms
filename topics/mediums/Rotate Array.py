from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,2,3,4,5,6,7], k = 3
        # shifting tthe aray to the right, what does it actually do 
        # we will realise upon looking at it
        # it actually causes like a reverse sort equation
        #upon closer inspection, what if reverse the whole aray 
        # and then revrese the portion, that i still sroted, and keep the unrversed portion, revresed
        #
        # [7, 6, 5, 4, 3, 2, 1, ]
        if len(nums) == 1:
            return
        k %= len(nums)
        def reverseList(index, end):
            left = index
            right = end
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        reverseList(0, len(nums) -1)
        reverseList(k, len(nums) -1)
        reverseList(0,k - 1)



        
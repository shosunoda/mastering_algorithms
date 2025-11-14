class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0,0,1,1,1,2,2,3,3,4]
        # how do we count unique elemnts as we pass in a sorted array 
        # here, its pretty clear that if its sorted, ,then adjacent bumbers are bundled together
        #
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left 
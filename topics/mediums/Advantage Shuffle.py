from typing import List
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        # given that we have num1s and num2 sorted
        # lets go through them individuall from ascending order
        # if an elmeent in nums1 is larger than an aelemtn in nums2 
        # we can place an element there
        # if its not, we will try and place the element of num1 to the largest of num2 
        # and we continue this, 
        # this means we need to have a sroted map for nums2 that amps the value to its appropriate index 
        # and we need two pointers for this 
        nums2map = sorted([ (element, index) for index, element in enumerate(nums2)])
        left = 0
        right = len(nums1) - 1
        result = [0] * len(nums1)
        for num in nums1:
            if num > nums2map[left][0]:
                result[nums2map[left][1]] = num
                left += 1
            else:
                result[nums2map[right][1]] = num
                right -= 1
        return result
        
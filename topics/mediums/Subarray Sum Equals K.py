from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
#
        # a subarraay can be seen as a total from a starting point and a endpoint right
        # if we look at it smartly, it can also be seen as operation between two subarrays
        # subarray[a:b] = subarray[:b]  - subarray[:a] 
        # so if you sbtract all the poitns from a from all the points of b, you get the subarray from a to be
        # so yeah, thats hoe we calcualte all subarrays within one pass 
        # and then we use a map to further tke adtvantage of this
        #
        #
        #
        #
        #
        subarray_map = defaultdict(int)
        subarray_map[0] = 1
        total = 0
        answer = 0
        for num in nums:
            total += num
            if total - k in subarray_map:
                answer += subarray_map[total - k]
            subarray_map[total] += 1
        return answer
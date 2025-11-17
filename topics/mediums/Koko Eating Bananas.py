from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        # this is binary search becaue we are told to find a minimum value 
        # among a range of possible values
        # and these possibels are monotic such that once a value si true, any value greater than it will also be true
        # and we want to find the first instance in which itis true 
        #
        def hourstoeat(rate):
            time = 0
            for pile in piles:
                time += math.ceil(pile / rate)
            return time 
        while left <= right: 
            mid = (left + right) // 2
            if hourstoeat(mid) <= h:
                right = mid - 1
            else:
                left = mid  + 1
        return left 


        
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # so firstly, i think we have to try and understand how to represent this algorihtmically
        # so to first do that, lets try and see whether we can compute the same result withthe test case
        # using manually 
        #[0,1,0,2,1,0,1,3,2,1,2,1]
        # # already theres some form of insight, we need a left_max and a right_max
        #  max(0, min(left_max, right_max) - col[i])
        # so i think very clearly the formula looks like this 
        # we need to maintain a left_max clearly, to rpresent the border on the left side
        # and a right_max for the right_side
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        # [0,0, 1, 1, 2, 2, 2, 2, 3, 3, 3,]
        #[, 2 , 1,0]
        left_max = [0]
        for num in height:
            left_max.append(max(left_max[-1], num))
        right_max = [0]
        for num in reversed(height):
            right_max.append(max(right_max[-1], num))
        right_max = right_max[::-1]
        result = 0
        for index, num in enumerate(height):
            left_cap = left_max[index]
            right_cap = right_max[index]
            result += max(0, min(left_cap, right_cap) - num)
        return result
        
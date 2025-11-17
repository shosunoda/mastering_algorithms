from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # lets think about this 
        # so the amount of water a caontqiner can store is defined by this formula 
        # min(height1, height2) * width 
        # right
        # and what we want to is, we want to maximise this value
        # obviously the most obvous brute force solution would be to 
        # do this n^2
        # where we have a initial loop from start to ened cal this i
        # and then a second loop from i to end, where we compute the 
        # every possible container 
        # now, my question is, is there anyw asted computations here that we can get rid of 
        #
        # 1 * 8 = 8 
        # however, looking at this, its farily easy to see that 
        # theres no point computong the rest of the containers using 1 
        # as aour collumn, when we have a collumn thats next to it thats of length 8, and only one dith short
        # so already, based on this, we can see a shortcut in which we can trim some evaluation that we dont need to do
        # how do we deifne this further to make it a conret algorhtm 
        # one thing we can realise from this is 
        # the only two ways to increase our formula for one i gave above is to increase the minimum height or the wideth
        # and letsay the wideth is maximised, that means the only way to increase is to increase the minimum height, how would we do that, we would do that by changing the smaller height to the next index in opes that our limit is changed
        # idk how i would process this thought succidnly in an itberview setting thoug
        left = 0 
        right = len(height) - 1
        answer = 0 
        while left < right: 
            left_height = height[left]
            right_height = height[right]
            answer = max(answer, (right - left) * min(right_height, left_height))
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        return answer
        

        
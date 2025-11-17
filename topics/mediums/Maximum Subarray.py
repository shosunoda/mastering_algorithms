from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # compute every subarray sum, and then return that 
        # however thats n^2 because we are going to have two for loops the initial one that lopos between 1 and n 
        # hich we call i, and the second i to n, which we call j
        # n(n-1)= n^ - n
        # which is roughly n^2 time
        # so the question how woeuld we optimise this 
        #[-2,1,-3,4,-1,2,1,-5,4]
        # -2, -1, 
        # already we see this insight, there are some conditions in which we just shouldnt add a value
        #like here, starting from -2 gives no value over starting at 1
        # 1, -2, 2 
        # we see this pattern agian, with 4 its better to start at at 4 then to end start at all elemebts prior to it
        # because the total starting from there is greater than 
        # 4, 3 5, 6, 1, 5
        # we start realising that maybe its possibe to compute the largest subarray in one pass using this pattern identified
        # what we realised is that we can invalidate starting points ofn array if there is no value to starting there comapred to a later point
        # so what this means numerically is that if start > total + start, its better of to start fresh from start 
        # and if we use this condition, we realise we can do this in one pass because we only have go through the array once to invalid the bad indexes, and as long as keep a running max of the longest subarray, we should be able to compute it
        answer = - float('inf')
        total = 0 
        for num in nums:
            total += num
            if num > total:
                total = num
            answer = max(total, answer)
        return answer

        
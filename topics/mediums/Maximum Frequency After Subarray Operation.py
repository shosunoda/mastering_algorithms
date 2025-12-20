from typing import List
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # so we ant to find the maxium frequency of the value k after doing a operation 
        # this means we want to choose a subarray that would maximise the gain in elements of k
        # how do we determine that subarray 
        # for the operation to be defined, we have to choose two 3 numebrs, starting boundary, end boundary as well as the intgere itself 
        # now wehen look at the contraitns of this question, we see that elements are bounded between 50 and 1
        # and so is k
        # what does this mean, x = k - a where a is an element of the list 
        # because there are only 50 possible attempts, we can actually try and compute all possible x's, to compute all possible subarray gains
        # which would be defined as 50(n), which is still o(n)
        # # for each possible x, we will say that you gained an element if a + x = k, and you missed an element if a = k 
        #, we want to compute maxiumum gain from this and add it to our original 
        original_count = nums.count(k)
        max_gain = 0
        for x in range(-49, 51):
            cur_gain = 0 
            for index in range(len(nums)):
                cur_element = 0
                if nums[index] == k:
                    cur_element = -1
                elif k - nums[index] == x:
                    cur_element = 1
                cur_gain = max(cur_gain + cur_element, cur_element)
                max_gain = max(max_gain, cur_gain)
        print(f"original count is {original_count}", f"max_gain is {max_gain}")
        return original_count + max_gain
        
        # element a + x == k 
        # what are the possible founds for x 
        #k - a == x
        # maximum is 50, minium = 0 
        # 
        
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we have to return the actual triplets that result in a total of 0 
        # right
        #  [-1,0,1,2,-1,-4]
        # lets consider this input right
        # if we start with -1, what are the two ohter inputs that we can take in 
        # that would be both 1 and 0 right
        # but whats the lgoic behind this, we have the initial number 1, now we are trying to find snumbers that sum up to -1 
        # how would we do that given therest of the array 
        # in the most efficient implementation
        # obviously, the brute force solution requires us to iterate through every single triplet 
        # that will look like three for loops chained with each other 
        # hwoever thats too long
        # i think we can take inspiration from two sum
        # where if we fix a digit in the array
        # we can actually make it a two sum question
        # as i mentiond just now, consider the first index to be a target number
        # now we just have to find two indexes j and k, such that they do equal the target
        # for this to work, we would have to first sort the array to make monotoic, and take advtange of this propery
        # if its a monotic propery, we can gurantee that every nuber to the right >= to the number left right
        # this allows us to use 2 pointers 
        # if have a let piointer starting from the lhs, and the righ tpointer starting from rhs
        # we can check if its larger than the sum if its, we decrease the right pointer, because we know all numbers to the right of the right pointer are invalid, and thus effecctively removing those domension spacs 
        # this works because we know the left pointr erpresents the smalelstnumber we can use, and the right hand side repsentats the largest, so only way to move target is to move right pointer
        # now, there are actually muplte edge cases that exist hre
        # we don't want to reprocess duplicates, when does a duplication condition occur in a sorted array 
        # [-1,-1, -1, 1, 1, 2 , 3 , 4]
        #  so we can only have -1, -1 + 2 once
        # since its sortd, if we face a duplicate, it will be in the adjacent indexes right
        # how do we ensure, we process double tuples only once
        #  this only occurs if there are three in a row?
        # no cause even if its just two ina row, we will consider -1, 0, 1 
        # twice
        # so we can skip duplicates by checking prev == current
        # now how do check we dont process duplicates in the doubel pointer stuff 
        # we only encounter duplicares if the second index is the same right
        # so to avoid processing the same tuplets in the pointer logic, we can just skip the same indexes until its out of index
        # cause if two numbers are fixed, theres only answer, so we just haveto ensure at least one of the numbers are different
        result = []
        nums.sort()
        for i in range(len(nums)):
            initial = nums[i]
            if i != 0 and initial == nums[i -1]:
                continue
            left = i + 1
            right = len(nums) - 1
            #  [-1,0,1,2,-1,-4]
            # [-4, -1, -1, 0, 1, 2]
            while left < right:
                total = initial + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplet = [initial, nums[left], nums[right]]
                    result.append(triplet)
                    prev_left = nums[left]
                    while left < right and prev_left == nums[left]:
                        prev_left = nums[left]
                        left += 1
        return result




        
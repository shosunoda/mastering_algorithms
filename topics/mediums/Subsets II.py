from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # we want to return all possible subsets that dont have duplictes right
        # firstly, to find all possible subses in the first place
        # at each index, you have 2 choices, to include it or exlcude it 
        # thats how you generate all possible subsets regardless of whether it has duplicates
        # so how do we want to avoid adding duplicates is the question 
        # when do you duplicates 
        # these are the questions tthat have to somehow solve 
        # [1, 2, 2]
        #       []      [1]
        #.    []  [2]  [1] [1,2] 
        #.   []  [2] [2] [2,2 ]
        #   we encounter duplicates in this decision tree, why do we encounte
        # we encountet it here because wechoose to process 2 again even after we should ahve already process it
        # and the only valid process of 2 tht can occur twice is when we consider adding two twos 
        # so tahts the problem 
        nums.sort()
        result = []
        def dfs(index, path):
            if index == len(nums):
                result.append(path[:])
                return
            path.append(nums[index])
            dfs(index + 1, path)
            path.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            dfs(index + 1, path)
            return
        dfs(0, [])
        return result

        
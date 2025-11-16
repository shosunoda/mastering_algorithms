from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i think  if its sorted and done in a one index array, and we have to return the indexes 
        # we can have two methods, one to use a binary search, or two pointers, or the other one to use a map
        # the map will have the value in nums and the index as a key value pair 
        # if we ever encounter a value later on that requires that avalue in unms to form target, we can just return it 

        seen = {}
        for index, num in enumerate(numbers):
            if target - num in seen:
                return [seen[target - num] + 1, index + 1]
            seen[num] = index
        return [-1, -1]
        
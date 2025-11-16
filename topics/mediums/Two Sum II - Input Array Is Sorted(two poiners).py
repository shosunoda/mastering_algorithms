from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i think  if its sorted and done in a one index array, and we have to return the indexes 
        # we can have two methods, one to use a binary search, or two pointers, or the other one to use a map
        # the map will have the value in nums and the index as a key value pair 
        # if we ever encounter a value later on that requires that avalue in unms to form target, we can just return it 
        left = 0 
        right = len(numbers ) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]
        
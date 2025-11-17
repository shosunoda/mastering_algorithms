from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we have to return the array that represents the number od days we have to after ith day to get a warmer temperature
        #
        # [73,74,75,71,69,72,76,73]
        # we can only get the answer aftwe we travel past the current index right
        # we see 73, and then see 74 --> we then have to somehow put the difference in indeexs 
        # at 73, and then for 74, --> we see 75, dot he same thing
        # what happens for 75, we see 71, 69, 72 
        # based on this, it look slike decreasing stack 
        # i think we need to store two values being the index, and the value itself
        # as we process index, we try and pop everything smaller than it 
        result = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prev_index, prev_temp = stack.pop()
                result[prev_index] = index - prev_index
            stack.append((index, temp))
        return result
        
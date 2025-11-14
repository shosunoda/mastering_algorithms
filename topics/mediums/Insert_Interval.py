from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # so there 
        # so how many cases are there 
        # I can ssee two edgs already, 
        # if the new iterval occurs before the ending point, lets just reurn it 
        # if the new interval occurs after all intervals, add it at the end 
        # now lets try and define whether the interval is overlapping or not
        # the intervals overlap only if they are not disjoint
        # they are disjoinst if the end of the new occur occur before the start of the current one 
        # or if the start of the new interval occur after
        # 1. 3
        #.     4.   6 
        # an interval disjoinst is the new interval start > cur_ end or # new end is < cur_ start 
        # if new_end >= cur_start and new_start <= cur_end
        #once we encounter this condition, we have to consider minimising and maximisng the endpoints 
        result = []
        new_start, new_end = newInterval
        for index, (cur_start, cur_end) in enumerate(intervals):
            if new_end < cur_start:
                result.append([new_start, new_end])
                return result + intervals[index:]

            elif new_start > cur_end:
                result.append([cur_start, cur_end])
                
            else:
                new_start = min(cur_start, new_start)
                new_end = max(cur_end, new_end)
        result.append([new_start, new_end])
        return result

        
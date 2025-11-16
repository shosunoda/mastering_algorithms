from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [[1,3],[2,6],[8,10],[15,18]]
        # 1 -- - 3
        #. 2 ---------- 6
        #.                 8 === 10 
        #                               15 -- 18
        # firstly, lets define what an overlapping interval is
        # int his scenario its when beginning of an interval is before the end of an interval, and the the end of interval is after the end 
        # this is the contest of intervals being sorted in srat time 
        # so to more formally define htis, 
        # it would be when laterstart <= earlier_end and later end  is 
        # overlalping 
        # when its overlapimg, we should update end points as well because later intervals might also be overlaping
        # so the question is when can we add intervals as we process them
        # well if go witht his method, we can only add intervals after we see the subsquent one 
        # when is it not overlapping, its not overlapping when the beginning of the second_start > earlier end
        #
        # but ya, we should also go through an example just to make sure 
        if not intervals:
            return []
        intervals.sort(key = lambda x: (x[0], x[1]))
        prev_start, prev_end = intervals[0]
        result = []
        for start, end in intervals[1:]:
            if start <= prev_end:
                prev_end = max(prev_end, end)
                prev_start = min(start, prev_start)
            else:
                result.append([prev_start, prev_end])
                prev_start, prev_end = start, end
        result.append([prev_start, prev_end])
        return result


        
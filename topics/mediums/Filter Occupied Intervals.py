class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        occupiedIntervals.sort(key = lambda x: x[0]) # this is to sort byf first elmeent 
        prev_start, prev_end = occupiedIntervals[0]
        merged_intervals = []
        # what are the cases for two intervals where the first one has ealier start 
        #  we should merge when the second interval start is < or equal to first one  end + 1 
        #  how should we reassign varibale,s prev_ end should just be max(cur_end, prev_end)
        #  and then at the end, we dont insert the interval, so we should we insert it after the iteration
        for cur_start, cur_end in occupiedIntervals[1:]: 
            if cur_start <= prev_end + 1:
                prev_end = max(cur_end, prev_end)
            else:
                merged_intervals.append([prev_start, prev_end])
                prev_start = cur_start
                prev_end = cur_end
        merged_intervals.append([prev_start, prev_end])

        # removeing 
        new_intervals = []
        for cur_start, cur_end in merged_intervals: 
            if cur_end < freeStart or cur_start > freeEnd:
                new_intervals.append([cur_start, cur_end])
            else:
                if cur_start < freeStart:
                    new_intervals.append([cur_start, freeStart -1])
                if cur_end > freeEnd:
                    new_intervals.append([freeEnd + 1, cur_end])
        return new_intervals
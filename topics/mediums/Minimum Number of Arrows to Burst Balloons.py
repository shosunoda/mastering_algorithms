class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # [[10,16],[2,8],[1,6],[7,12]]
        #1.   6 
        # 2.      8
        #        7.   12
        #.          10.     16
        # minimum number of arrows = maximise number of ballons hit per arrow 
        # baloons can be burt by same arrow if their x radius is overlapping 
        # so we probably have to sort by interval start time again right
        # this is because when sorting them by start time, you get the porpery that 
        # overlaps only happen to conseuctive intervals 
        # when a n itverla occur, we have a property that earlier starts are ealier than the current one 
        # what does that mean for overlapping b start < a end 
        # it means that any overlaping intervals with i has to come from prior ones right
        # this allows ut reason about local propertie sand convert it to global roperties 
        # when two intervals overlap, we want to take the shorter end right 
        # cause we need to ensure we hit that witha arrrow as well 
        #and so when a we see a interval doesnt overlap, we need a new arrow 
        points.sort(key = lambda x: (x[0],x[1]))
        arrows = 0 
        prev_end = -float('inf')
        for start, end in points:
            if start <= prev_end:
                prev_end = min(prev_end, end)
            else:
                prev_end = end
                arrows += 1
        return arrows



        
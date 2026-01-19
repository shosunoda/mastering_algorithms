from heapq import heapify, heappush, heappop
from typing import List
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # capciacty empty seats 
        # vehicle only drives east 
        # capacity and an array trips 
        # trips has tuple num, from, and to 
        # true if it poss ible to kpick and drop of all passangers for given 
        #
        # [[2,1,5],[3,3,7]] capacity = 4
        #  so it can only go one way the car 
        # kinda like an interval question 
        # start from start 1, which is 1, and get two people, 
        # and then once we get off 
        # next intevral, theres more people 
        #  to overlap, we check if its beyodn cap, if its its false 
        trips.sort(key = lambda x: x[1])
        prev_dst = - float('inf')
        departure = []
        cur = 0
        for num, src, dst in trips:
            while departure and departure[0][0] <= src:
                cur -= heappop(departure)[1]
            if cur + num > capacity:
                return False
            cur += num
            heappush(departure, (dst, num))
        return True
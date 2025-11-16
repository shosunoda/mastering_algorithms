from heapq import heappush, heappop
import bisect
# like lets see i assume we haev to keep track of the size, some pointers for 
# we have to keep track of size of the array, and i think that should be it
# cause given the size of an array, if its even, we can easily determine 
# which two values we need
# that would be 
# 6 // 2 = 3, and 3 - 1
# 2, 3 
# and if its odd 
# 7 // 2 + 4
# and that should be it I think?
# dont see this why wouldnt work?
#[0, 1, 2, 3, 4, 5]
class MedianFinder:

    def __init__(self):
        self.large = [] # this will be min_heap
        self.small = []
        

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)

        if self.large and -self.small[0] > self.large[0]:
            heappush(self.large, -heappop(self.small))

        if len(self.small) > len(self.large) + 1:
            heappush(self.large, -heappop(self.small))
        elif len(self.large) > len(self.small):
            heappush(self.small, -heappop(self.large))


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
#
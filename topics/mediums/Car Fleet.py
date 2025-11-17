from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #  12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
        # destiantion = 12 miles
        #  [(0, 1), (3, 3), (5, 1), (8, 4), (10, 2)]
        #   takes 1 hours, 1 hour, 7 hours, 3 hours, 12 hours 
        # very clearly, we need to process them in terms of speed and position
        # why, so firtly we weant to start from the position closest to the destination
        # and then process the time of arrival then
        # if a time is faterh than the oens already processd, we know it becomes a fleet 
        # and the number of fleets is the nmber of cars that get merged 
        #
        processed = sorted(zip(position, speed), reverse = True)
        speed = [(target - position)/ speed for position, speed in processed]
        stack = []
        for time in speed:
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)
        